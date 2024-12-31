from .sst_paper import generate_and_save_structure_plot
import pandas as pd
# from .dssp import DSSP_PATH  # 确保路径正确
import tempfile
import os
import subprocess
import csv
from concurrent.futures import ThreadPoolExecutor
 
def run_dssp(pdb_file):
    if not os.path.exists(pdb_file):
        raise FileNotFoundError(f"PDB file not found: {pdb_file}")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".dssp") as temp_dssp_file:
        temp_dssp_path = temp_dssp_file.name

    try:
        command = ['mkdssp', "-i", pdb_file, "-o", temp_dssp_path]
        subprocess.run(command, check=True, capture_output=True, text=True)        
        return temp_dssp_path
    except subprocess.CalledProcessError as e:
        print(f"Error running DSSP: {e.stderr}")
        raise

def del_dssp(dssp_file):
    if os.path.exists(dssp_file):
        os.remove(dssp_file)

def process_and_save_row(row, pdb_file, save_folder):
    """
    处理单个任务，并将结果立即保存到 CSV 文件。
    """
    p1, p2 = row['protein1'], row['protein2']
    protein1_pdb = os.path.join(pdb_file, f'{p1}.pdb')
    protein2_pdb = os.path.join(pdb_file, f'{p2}.pdb')
    protein1_dssp = run_dssp(protein1_pdb)
    protein2_dssp = run_dssp(protein2_pdb)
    try:
        if 'chain1' in row:
            a = row['chain1'].split(';')
            b = row['chain2'].split(';')
            VSS, SPS = generate_and_save_structure_plot(
                p1, p2, protein1_pdb, protein2_pdb, protein1_dssp, protein2_dssp, save_folder,
                chainid1=a, chainid2=b
            )
        else:
            VSS, SPS = generate_and_save_structure_plot(
                p1, p2, protein1_pdb, protein2_pdb, protein1_dssp, protein2_dssp, save_folder
            )

        # 立即保存结果
        output_file = os.path.join(save_folder, 'MELO_score.csv')
        with open(output_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([p1, p2, VSS, SPS])

        print(f"Processed and saved: Protein1={p1}, Protein2={p2}, VSS={VSS}, SPS={SPS}")
    finally:
        # 清理临时 DSSP 文件
        del_dssp(protein1_dssp)
        del_dssp(protein2_dssp)

def process_file(protein_file, pdb_file, save_folder, threads=4):
    """
    多线程处理文件，每完成一行立即保存结果。
    """
    protein_pairs = pd.read_csv(protein_file)
    output_file = os.path.join(save_folder, 'MELO_score.csv')

    # 创建 CSV 文件并写入表头
    if not os.path.exists(output_file):
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Protein1', 'Protein2', 'VSS', 'SPS'])

    # 多线程处理
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for _, row in protein_pairs.iterrows():
            executor.submit(process_and_save_row, row, pdb_file, save_folder)

def melo(protein_file, pdb_file, save_folder, threads=4):
    process_file(protein_file, pdb_file, save_folder, threads)

def main():
    # 示例参数
    protein_file = "/mnt/e/topic/mutant_protein_structure/MELO/test_data/protein_pairs.csv"  # 输入的蛋白质对文件
    pdb_file = "/mnt/e/topic/mutant_protein_structure/MELO/test_data/pdb"       # PDB 文件所在文件夹
    save_folder = "/mnt/e/topic/mutant_protein_structure/MELO/test_data/result"         # 结果保存的文件夹
    threads = 4                         # 设置线程数

    # 运行多线程任务
    process_file(protein_file, pdb_file, save_folder, threads)

if __name__ == "__main__":
    main()