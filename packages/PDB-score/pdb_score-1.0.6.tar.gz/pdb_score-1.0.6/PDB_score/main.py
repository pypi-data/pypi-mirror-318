import argparse
import os
from .core import parse_pdb_files, calculate_score
from .ProteinStructure import ProteinStructure


def main():
    parser = argparse.ArgumentParser(description="Calculate protein scores based on PDB files.")
    parser.add_argument("-c", "--control", required=True, help="Experimental PDB file directory")
    parser.add_argument("-t", "--treatment", required=True, help="Predicted PDB file directory")
    parser.add_argument("-o", "--output", required=True, help="Output directory for saving scores")
    parser.add_argument("-T", "--Threat", required=False, type=int, default=4, help="Specify the number of cores, default is 4")
    parser.add_argument("-B", "--Batch", required=False, type= int, default=5000, help="Specify the batch size, default is 5000")
    args = parser.parse_args()

    control_dir = args.control
    treatment_dir = args.treatment
    output_dir = args.output
    thread_count = args.Threat
    batch_size = args.Batch

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 解析 PDB 文件
    print("Start parsing control PDB files")
    atoms_control = parse_pdb_files(control_dir, batch_size=batch_size, thread_count=thread_count)
    print("Start parsing treatment PDB files")
    atoms_treatment = parse_pdb_files(treatment_dir, batch_size=batch_size, thread_count=thread_count)

    # 为同名文件创建 ProteinStructure 类
    protein_structures = []
    for file_name in atoms_control.keys():
        if file_name in atoms_treatment:
            protein_structure = ProteinStructure(
                name=file_name,
                atom_control=atoms_control[file_name],
                atom_treatment=atoms_treatment[file_name]
            )
            protein_structures.append(protein_structure)


    # 计算评分并保存结果
    # 替代逐行追加列表，用生成器写入 CSV
    with open(os.path.join(output_dir, 'protein_scores.csv'), 'w', encoding='utf-8') as output_csv:
        head = "name,RMSD," + ",".join([f"{2 ** i}A" for i in range(8)]) + ",Average\n"
        output_csv.write(head)
        for protein in protein_structures:
            scores = {}
            rmsd = protein.alignment()
            protein.get_distances()  # 获取延迟计算的距离
            for times in range(8):
                limit = 2 ** times
                score = calculate_score(protein, limit)
                scores[f'{limit}A'] = score if score is not None else 0
            scores['Average'] = int(sum(scores.values()) / len(scores))

            # 写入数据为行
            line = f"{protein.name},{rmsd:.4f}," + ",".join(map(str, scores.values())) + "\n"
            output_csv.write(line)
    print(f"Score is saved to {output_dir}/protein_scores.csv")



if __name__ == "__main__":
    main()