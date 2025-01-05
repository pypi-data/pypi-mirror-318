import os
from multiprocessing import Pool
from pathlib import Path
from functools import partial

import numpy as np
from Bio.PDB import PDBParser

from .alignment import align_structures


# 提取中心碳原子坐标
def extract_ca_coordinates(structure):
    ca_coords = [
        residue['CA'].coord
        for model in structure
        for chain in model
        for residue in chain.get_residues()
        if residue.id[0] == ' ' and 'CA' in residue
    ]
    return ca_coords


# 批量解析最多 batch_size 个 PDB 文件
def parse_pdb_files(directory, batch_size=5000, thread_count=4):
    pdb_path = Path(directory)
    # pdb_files = [pdb_file.as_posix() for pdb_file in pdb_path.glob("*.pdb")]
    # 查找 .pdb 和 .ent 文件
    pdb_files = [pdb_file.as_posix() for pdb_file in pdb_path.glob("*.pdb")] + \
                [ent_file.as_posix() for ent_file in pdb_path.glob("*.ent")]
    print(f"Batch size = {batch_size}, Total files = {len(pdb_files)}")
    print(f"Using {thread_count} CPU cores...")


    # 每次处理 batch_size 数量的文件
    all_results = {}
    for i in range(0, len(pdb_files), batch_size):
        batch_files = pdb_files[i:i + batch_size]
        print(f"Processing batch {i // batch_size + 1}: {len(batch_files)} files...")

        # 使用多进程处理每个文件
        with Pool(thread_count) as pool:
            batch_results = pool.map(parse_single_pdb_file, batch_files)

        # 将结果保存到总结果字典
        all_results.update(dict(batch_results))

    return all_results


def find_common_files(control_path, treatment_path):
    # 获取 control_path 下所有 .pdb 和 .ent 文件
    control_pdb_files = [f for f in Path(control_path).glob("*.pdb")] + [f for f in Path(control_path).glob("*.ent")]
    # 获取 treatment_path 下所有 .pdb 和 .ent 文件
    treatment_pdb_files = [f for f in Path(treatment_path).glob("*.pdb")] + [f for f in
                                                                             Path(treatment_path).glob("*.ent")]

    # 提取文件名（不含扩展名）集合
    control_file_set = set(os.path.splitext(f.name)[0] for f in control_pdb_files)
    treatment_file_set = set(os.path.splitext(f.name)[0] for f in treatment_pdb_files)

    # 找到相同的文件名（交集）
    common_file_set = control_file_set & treatment_file_set

    # 构建包含扩展名的文件路径对列表
    common_files = []
    for common_file in common_file_set:
        # 在 control 和 treatment 路径分别查找
        control_file_with_ext = next((f for f in control_pdb_files if f.stem == common_file), None)
        treatment_file_with_ext = next((f for f in treatment_pdb_files if f.stem == common_file), None)
        if control_file_with_ext and treatment_file_with_ext:
            common_files.append((control_file_with_ext, treatment_file_with_ext))

    print(f"Found {len(common_files)} common files.")
    return common_files



def align_parse_pdb_files(Control, Treatment, batch_size=2500, thread_count=4, threshold=1.0, max_iterations=10, save_limit=1.0,):
    control_path = Path(Control)
    treatment_path = Path(Treatment)

    # 查找 control_path 和 treatment_path 下同名的 .pdb 和 .ent 文件（包含拓展名）
    common_files = find_common_files(control_path, treatment_path)
    
    print(f"Batch size = {batch_size}, Total files = {2 * len(common_files)}")
    print(f"Using {thread_count} CPU cores...")

    batch = int(batch_size/2)

    # 每次处理 batch_size 数量的文件
    all_results = {}
    for i in range(0, len(common_files), batch):
        batch_files = common_files[i:i + batch]
        print(f"Processing batch {i // batch + 1}: {len(batch_files)} file pairs...")

        align_prase_pdb_partial = partial(align_prase_pdb, threshold=threshold, max_iterations=max_iterations, save_limit=save_limit)

        # 使用多进程处理每个文件
        with Pool(thread_count) as pool:
            batch_results = pool.map(align_prase_pdb_partial, batch_files)

        # 将结果保存到总结果字典
        all_results.update(dict(batch_results))

    return all_results
    
    


# 单个文件解析，提取 CA 原子坐标
def parse_single_pdb_file(file_path):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(file_path, file_path)
    return os.path.splitext(os.path.basename(file_path))[0], extract_ca_coordinates(structure)


# 对齐解析
def align_prase_pdb(file_pair, threshold, max_iterations, save_limit):
    control_path = file_pair[0]
    treatment_path = file_pair[1]
    control_name = os.path.splitext(os.path.basename(control_path))[0]
    control_coordinates, treatment_coordinates = align_structures(control_path, treatment_path, threshold, max_iterations, save_limit)
    return control_name, (control_coordinates, treatment_coordinates)



# 优化的 protein 评分计算
def calculate_score(protein, limit):
    limit = float(limit)

    distances = protein.get_distances()

    score = np.sum(distances < limit)
    return int(score / protein.initial_length * 100)


if __name__ == "__main__":
    control_path = r"C:\Users\hydro\OneDrive\code\pdb_score\output_fold\ture_structure\pet80"
    treatment_path = r"C:\Users\hydro\OneDrive\code\pdb_score\output_fold\esm_v1\pet80"

    res = align_parse_pdb_files(control_path, treatment_path)
    print(len(res))
