import numpy as np
from Bio.PDB import PDBParser


def read_all_chains_from_pdb(file_path):
    """
    从 PDB 文件中提取所有链的 Cα 原子坐标和残基简称。
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("structure", file_path)

    chains_data = {}
    for model in structure:
        for chain in model:
            chain_id = chain.id
            coords = []
            residue_names = []

            for residue in chain:
                if "CA" in residue:
                    ca_atom = residue["CA"]
                    coords.append(ca_atom.coord)
                    residue_names.append(residue.resname)

            if coords:
                chains_data[chain_id] = {
                    "coords": np.array(coords),
                    "residue_names": residue_names
                }

    return chains_data


def longest_common_subsequence(seq1, seq2):
    """
    找到两个序列的最长公共子序列（LCS）。
    """
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    lcs_indices = []
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_indices.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_indices.reverse()
    return lcs_indices


def calculate_centroid(coords):
    """
    计算一组点的质心。
    """
    return np.mean(coords, axis=0)


def kabsch_algorithm(P, Q):
    """
    使用 Kabsch 算法计算最优旋转矩阵。
    """
    covariance_matrix = np.dot(P.T, Q)
    V, S, W_t = np.linalg.svd(covariance_matrix)
    d = np.linalg.det(np.dot(V, W_t))
    D = np.diag([1, 1, np.sign(d)])
    return np.dot(np.dot(V, D), W_t)


def transform_coordinates(coords, rot_matrix, translation_vector):
    """
    对坐标进行旋转和平移操作。
    """
    return np.dot(coords, rot_matrix.T) + translation_vector


def iterative_superposition(P, Q, threshold, max_iterations=10, save_limit=0.9):
    """
    基于迭代的叠加算法，对坐标点集 Q 叠加到点集 P。
    """
    min_size = min(len(P), len(Q))
    required_size = int(min_size * save_limit)

    iteration_count = 0
    while True:
        indices = np.arange(min(len(P), len(Q)))
        prev_indices = None

        while not np.array_equal(indices, prev_indices):
            prev_indices = indices

            P_subset = P[indices]
            Q_subset = Q[indices]

            P_centroid = calculate_centroid(P_subset)
            Q_centroid = calculate_centroid(Q_subset)

            P_centered = P_subset - P_centroid
            Q_centered = Q_subset - Q_centroid

            rotation_matrix = kabsch_algorithm(P_centered, Q_centered)

            Q_transformed = transform_coordinates(
                Q, rotation_matrix, P_centroid - np.dot(Q_centroid, rotation_matrix.T))

            distances = np.linalg.norm(P - Q_transformed, axis=1)
            indices = np.where(distances <= threshold)[0]

            if len(indices) < required_size:
                threshold *= 1.2

        if len(indices) >= required_size:
            final_Q = transform_coordinates(
                Q[indices], rotation_matrix, P_centroid - np.dot(Q_centroid, rotation_matrix.T))
            return P[indices], final_Q

        iteration_count += 1
        threshold *= 2.0
        if iteration_count >= max_iterations:
            raise ValueError(
                f"Exceeded max iterations. Matched: {len(indices)}, Required: {required_size}")


def find_best_chain_pair(data_1, data_2):
    """
    比较两个 PDB 文件中的所有链，寻找最佳匹配链。
    """
    matched_chains = []

    for chain_1_id, chain_1_data in data_1.items():
        for chain_2_id, chain_2_data in data_2.items():
            lcs_indices = longest_common_subsequence(
                chain_1_data['residue_names'], chain_2_data['residue_names'])
            if len(lcs_indices) >= 5:
                matched_chains.append((chain_1_id, chain_2_id))

    return matched_chains


def align_structures(file_path_1, file_path_2, threshold=1.0, max_iterations=10, save_limit=0.9):
    """
    入口函数：对两个 PDB 文件进行对齐，返回 P_final 和 Q_final。

    :param file_path_1: 第一个 PDB 文件路径
    :param file_path_2: 第二个 PDB 文件路径
    :param threshold: 距离阈值，用于确定匹配
    :param max_iterations: 最大迭代次数
    :param save_limit: 保存比例（定义对齐点数的最低限制）
    :return: P_final, Q_final - 对齐后的坐标点集
    """
    # 提取两个文件的链数据
    data_1 = read_all_chains_from_pdb(file_path_1)
    data_2 = read_all_chains_from_pdb(file_path_2)

    # 匹配最佳链对
    matched_chains = find_best_chain_pair(data_1, data_2)
    if not matched_chains:
        raise ValueError("No matching chains found between the two files.")

    # 默认使用第一个匹配的链对
    match_chain_control, match_chain_treatment = matched_chains[0]
    chain_control = data_1[match_chain_control]
    chain_treatment = data_2[match_chain_treatment]

    P_coords = chain_control['coords']
    Q_coords = chain_treatment['coords']
    lcs_indices = longest_common_subsequence(chain_control['residue_names'], chain_treatment['residue_names'])

    P_matched = P_coords[[i for i, _ in lcs_indices]]
    Q_matched = Q_coords[[j for _, j in lcs_indices]]

    # 迭代叠加
    P_final, Q_final = iterative_superposition(P_matched, Q_matched, threshold, max_iterations, save_limit)

    return P_final, Q_final