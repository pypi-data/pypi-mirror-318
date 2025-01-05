from Bio.PDB import PDBParser, Superimposer
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist


class PDBProcessor:
    def __init__(self, pdb_path):
        """
        初始化 PDB 处理器
        :param pdb_path: PDB 文件路径
        """
        self.pdb_path = pdb_path
        self.parser = PDBParser(QUIET=True)
        self.structure = self.parser.get_structure("PDB", pdb_path)
        self.coordinates = self.extract_ca_coordinates()

    def extract_ca_coordinates(self):
        """
        从 PDB 文件中提取 Cα 原子坐标
        :return: NumPy 数组，包含所有 CA 原子的三维坐标
        """
        ca_coords = []
        for model in self.structure:
            for chain in model:
                for residue in chain.get_residues():
                    # 提取标准氨基酸残基的 CA 原子
                    if residue.id[0] == " " and "CA" in residue:
                        ca_coords.append(residue["CA"].coord)
        return np.array(ca_coords)

    @staticmethod
    def match_residues(coords1, coords2):
        """
        使用匈牙利算法，在两个残基坐标集合之间找到最佳匹配
        :param coords1: 第一个集合的坐标 (NumPy 数组)
        :param coords2: 第二个集合的坐标 (NumPy 数组)
        :return: (匹配后的 coords1, 匹配后的 coords2)
        """
        # 计算距离矩阵
        distance_matrix = cdist(coords1, coords2)

        # 使用匈牙利算法找到匹配
        row_indices, col_indices = linear_sum_assignment(distance_matrix)

        # 提取匹配结果
        matched_coords1 = coords1[row_indices]
        matched_coords2 = coords2[col_indices]

        return matched_coords1, matched_coords2

    @staticmethod
    def align_structures(coords1, coords2):
        """
        对两个坐标集合进行几何对齐，返回对齐后的坐标和 RMSD 值
        :param coords1: 参考坐标 (NumPy 数组)
        :param coords2: 目标坐标 (NumPy 数组)
        :return: (对齐后的 coords2, RMSD 值)
        """
        super_imposer = Superimposer()
        # 设置参考和目标坐标
        super_imposer.set(coords1, coords2)
        # 应用变换到目标坐标
        super_imposer.apply(coords2)
        rmsd = super_imposer.rms
        return coords2, rmsd

    @staticmethod
    def save_cleaned_coordinates(coords, output_path, chain_id="A"):
        """
        将清洗后的坐标保存为 PDB 文件
        :param coords: 清洗后的坐标 (NumPy 数组)
        :param output_path: 输出文件路径
        :param chain_id: 链标识符
        """
        with open(output_path, 'w') as f:
            for i, coord in enumerate(coords):
                x, y, z = coord
                f.write(
                    f"ATOM  {i + 1:>5}  CA  GLY {chain_id}{i + 1:>4}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00           C\n"
                )
            f.write("TER\nEND\n")