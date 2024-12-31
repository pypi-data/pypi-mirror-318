import math
from collections import defaultdict
import numpy as np
import pandas as pd
from Bio import pairwise2
from Bio.Align import substitution_matrices as matlist
from Bio.PDB.PDBParser import PDBParser

# from Bio.PDB.DSSP import DSSP
from .DSSP import DSSP

amino_acids = defaultdict(lambda: 'X')
amino_acids.update(
    {'ALA': 'A',
     'PHE': 'F',
     'CYS': 'C',
     # 'SEC': 'U',
     'ASP': 'D',
     'ASN': 'N',
     'GLU': 'E',
     'GLN': 'Q',
     'GLY': 'G',
     'HIS': 'H',
     'LEU': 'L',
     'ILE': 'I',
     'LYS': 'K',
     # 'PYL': 'O',
     'MET': 'M',
     'PRO': 'P',
     'ARG': 'R',
     'SER': 'S',
     'THR': 'T',
     'VAL': 'V',
     'TRP': 'W',
     'TYR': 'Y'})


def remove_nan_rows_cols(matrix):
    df = pd.DataFrame(matrix)
    df.dropna(how='all', axis=0, inplace=True)  # 删除全是 NaN 的行
    df.dropna(how='all', axis=1, inplace=True)  # 删除全是 NaN 的列
    filtered_matrix = df.to_numpy()
    return filtered_matrix


def align_sequences(seq1, seq2):
    # print(seq1)
    aligner = pairwise2.align.localds
    matrix = matlist.load("BLOSUM62")
    gap_open = -10
    gap_extend = -0.5
    alignments = aligner(seq1, seq2, matrix, gap_open, gap_extend)
    best_alignment = alignments[0]
    aligned_seq1 = best_alignment[0]
    aligned_seq2 = best_alignment[1]
    return aligned_seq1, aligned_seq2


def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm1 * norm2)
    score = 1 - similarity
    return score


def calculate_upper_right_avg(matrix):
    upper_right = matrix[np.triu_indices(matrix.shape[0], k=1)]
    avg = np.mean(upper_right)
    return avg


def drmsd_r(aligned_seq1, aligned_seq2, cord1, cord2):
    n = len(aligned_seq1)
    seq_data = np.full((n, n), np.nan)
    # seq_data = pd.DataFrame(0, index=range(n), columns=range(n))
    for i in range(n):  # 枚举氨基酸
        re1 = aligned_seq1[i]
        re2 = aligned_seq2[i]
        if re1 == 'N' or re2 == 'N':
            continue
        for j in range(i + 1, n):
            re3 = aligned_seq1[j]
            re4 = aligned_seq2[j]
            if re3 == 'N' or re4 == 'N':
                continue
            vec1 = np.array(cord1[i]) - np.array(cord1[j])
            vec2 = np.array(cord2[i]) - np.array(cord2[j])
            dis1 = math.sqrt(np.dot(vec1, vec1))
            dis2 = math.sqrt(np.dot(vec2, vec2))
            # seq_data[i][j] = seq_data[j][i] = math.fabs(dis1 - dis2) / (dis1 + dis2) / (
            #         1 + math.fabs(dis_seq1 - dis_seq2) / (dis_seq1 + dis_seq2))
            seq_data[i][j] = seq_data[j][i] = math.fabs(dis1 - dis2) / max(dis1, dis2)
    return seq_data


class single_protein_complete():
    def __init__(self, pdb_file, pdb_name, dssp_file):
        self.pdb_file = pdb_file
        self.pdb_name = pdb_name
        self.dssp_file = dssp_file
        # 创建PDB解析器对象
        parser = PDBParser()
        # 使用解析器读取PDB文件
        self.structure = parser.get_structure(pdb_name, pdb_file)
        self.model = self.structure[0]
        # atom_list = Selection.unfold_entities(self.model, 'A')
        # alpha_carbons = [atom for atom in atom_list if atom.get_name() == 'CA']
        # self.coordinates = [atom.get_coord() for atom in alpha_carbons]

    def find_misssion(self):
        miss = defaultdict(lambda: defaultdict(str))
        for i in self.structure.header['missing_residues']:
            miss[i['chain']][i['ssseq']] = amino_acids[i['res_name']]
        return miss

    def binary_search_insert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                # 目标值已存在于列表中，根据需要决定是否插入
                return mid
        # 左边界作为插入位置
        return low

    def secondary_structure_info(self):
        dssp = DSSP(self.model, self.dssp_file)
        vector = defaultdict(list)
        res = defaultdict(list)
        ss_data = defaultdict(list)
        AA_position = defaultdict(list)
        coordinates = defaultdict(list)
        for a_key in list(dssp.keys()):
            chain_id = a_key[0]
            resseq_id = a_key[1][1]
            res_inf = dssp[a_key]
            # res_vector = [res_inf[3], res_inf[4], res_inf[5], res_inf[7], res_inf[9], res_inf[11], res_inf[13]]
            res_vector = [res_inf[3], res_inf[4], res_inf[5], res_inf[6], res_inf[7], res_inf[8], res_inf[9],
                          res_inf[10], res_inf[11],
                          res_inf[12], res_inf[13]]
            # res_vector = [res_inf[3], res_inf[4], res_inf[5], res_inf[7], res_inf[9],
                # res_inf[11],
                # res_inf[13]]
            res_vector = [res if not np.isnan(res) else 0 for res in res_vector]
            resseq = res_inf[1]
            ss_code = res_inf[2]
            res_coordinates = res_inf[14]
            if 'A' <= resseq <= 'Z':
                res[chain_id].append(resseq)
                if res_inf[2] not in ["H", "B", "E", "G", "I", "P", "T", "S", "N"]:
                    ss_code = "C"
                ss_data[chain_id].append(ss_code)
                vector[chain_id].append(res_vector)
                AA_position[chain_id].append(resseq_id)
                coordinates[chain_id].append(res_coordinates)
        return AA_position, res, ss_data, vector, coordinates

    def info_complete(self, chainid='ALL'):
        chains = [chain.id for chain in self.model]
        miss = self.find_misssion()
        AA_position, res, ss_data, vector, coordinates = self.secondary_structure_info()
        if chainid == 'ALL':
            AA_position_all = []
            res_chain_all = []
            ss_chain_all = []
            vector_chain_all = []
            coordinates_chain_all = []
            for chain in chains:
                miss_chain = miss[chain]
                AA_position_chain = AA_position[chain]
                res_chain = res[chain]
                ss_chain = ss_data[chain]
                vector_chain = vector[chain]
                coordinates_chain = coordinates[chain]
                for position, value in miss_chain.items():
                    ind = self.binary_search_insert(AA_position_chain, position)
                    AA_position_chain.insert(ind, position)
                    res_chain.insert(ind, value)
                    ss_chain.insert(ind, "N")
                    vector_chain.insert(ind, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    coordinates_chain.insert(ind, np.array([0, 0, 0]))
                AA_position_all.extend(AA_position_chain)
                res_chain_all.extend(res_chain)
                ss_chain_all.extend(ss_chain)
                vector_chain_all.extend(vector_chain)
                coordinates_chain_all.extend(coordinates_chain)
            return AA_position_all, res_chain_all, ss_chain_all, vector_chain_all, coordinates_chain_all
        elif isinstance(chainid, str):
            if chainid in chains:
                miss_chain = miss[chainid]
                AA_position_chain = AA_position[chainid]
                res_chain = res[chainid]
                ss_chain = ss_data[chainid]
                vector_chain = vector[chainid]
                coordinates_chain = coordinates[chainid]
                for position, value in miss_chain.items():
                    ind = self.binary_search_insert(AA_position_chain, position)
                    AA_position_chain.insert(ind, position)
                    res_chain.insert(ind, value)
                    ss_chain.insert(ind, "N")
                    vector_chain.insert(ind, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    coordinates_chain.insert(ind, np.array([0, 0, 0]))
            return AA_position_chain, res_chain, ss_chain, vector_chain, coordinates_chain
        elif isinstance(chainid, list):
            AA_position_all = []
            res_chain_all = []
            ss_chain_all = []
            vector_chain_all = []
            coordinates_chain_all = []
            for chain in chainid:
                if chain in chains:
                    miss_chain = miss[chain]
                    AA_position_chain = AA_position[chain]
                    res_chain = res[chain]
                    ss_chain = ss_data[chain]
                    vector_chain = vector[chain]
                    coordinates_chain = coordinates[chain]
                    for position, value in miss_chain.items():
                        ind = self.binary_search_insert(AA_position_chain, position)
                        AA_position_chain.insert(ind, position)
                        res_chain.insert(ind, value)
                        ss_chain.insert(ind, "N")
                        vector_chain.insert(ind, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                        coordinates_chain.insert(ind, np.array([0, 0, 0]))
                    AA_position_all.extend(AA_position_chain)
                    res_chain_all.extend(res_chain)
                    ss_chain_all.extend(ss_chain)
                    vector_chain_all.extend(vector_chain)
                    coordinates_chain_all.extend(coordinates_chain)
            return AA_position_all, res_chain_all, ss_chain_all, vector_chain_all, coordinates_chain_all
        else:
            print('Chain not found  for {}'.format(self.pdb_name))
            return None, None, None, None, None



def aligh_match(pdb_file1, pdb_name1, dssp_file1, pdb_file2, pdb_name2, dssp_file2, chainid1='ALL', chainid2='ALL'):
    try:
        protein1 = single_protein_complete(pdb_file1, pdb_name1, dssp_file1)
        AA_position1, res1, ss_data1, vector1, coordinates1 = protein1.info_complete(chainid1)
    except FileNotFoundError:
        print(f"Error: File not found at {pdb_name1}")
        return None, None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None
    try:
        protein2 = single_protein_complete(pdb_file2, pdb_name2, dssp_file2)
        AA_position2, res2, ss_data2, vector2, coordinates2 = protein2.info_complete(chainid2)
    except FileNotFoundError:
        print(f"Error: File not found at {pdb_name2}")
        return None, None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None
    if res1 is not None:
        seq1 = ''.join(res1)
        seq2 = ''.join(res2)
        aligned_seq1, aligned_seq2 = align_sequences(seq1, seq2)
        aligned_seq1_ss = []
        aligned_seq2_ss = []
        aligned_seq1_vector = []
        aligned_seq2_vector = []
        score_engry = []
        score_engry_count = []
        aligned_seq1_coordinates = []
        aligned_seq2_coordinates = []
        position1 = -1
        position2 = -1
        n = len(aligned_seq1)
        for i in range(len(aligned_seq1)):
            if aligned_seq1[i] != '-':
                position1 += 1
                aligned_seq1_ss.append(ss_data1[position1])
                aligned_seq1_vector.append(vector1[position1])
                aligned_seq1_coordinates.append(coordinates1[position1])
            else:
                aligned_seq1_ss.append('N')
                aligned_seq1_vector.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                aligned_seq1_coordinates.append(np.array([0, 0, 0]))
            if aligned_seq2[i] != '-':
                position2 += 1
                aligned_seq2_ss.append(ss_data2[position2])
                aligned_seq2_vector.append(vector2[position2])
                aligned_seq2_coordinates.append(coordinates2[position2])
            else:
                aligned_seq2_ss.append('N')
                aligned_seq2_vector.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                aligned_seq2_coordinates.append(np.array([0, 0, 0]))
            if aligned_seq1[i] != '-' and aligned_seq2[i] != '-' and ss_data1[position1] != 'N' and ss_data2[
                position2] != 'N':
                aligned_seq1_score = cosine_similarity(vector1[position1], vector2[position2])
                score_engry.append(aligned_seq1_score)
                score_engry_count.append(aligned_seq1_score)
            else:
                score_engry.append('NaN')
        d_rmsd = drmsd_r(aligned_seq1_ss, aligned_seq2_ss, aligned_seq1_coordinates, aligned_seq2_coordinates)
        score_rmsd_matrix = remove_nan_rows_cols(d_rmsd)
        np.fill_diagonal(score_rmsd_matrix, 0)
        mean_score = np.mean(score_engry_count)
        mean_score_rmsd = calculate_upper_right_avg(score_rmsd_matrix)
        # if vector1[position1] == [0, 0, 0, 0, 0, 0, 0] or vector2[position2] == [0, 0, 0, 0, 0, 0, 0]:
        #  print(ss_data1[position1],ss_data2[position2])
        return aligned_seq1, aligned_seq2, aligned_seq1_ss, aligned_seq2_ss, aligned_seq1_vector, aligned_seq2_vector, score_engry, score_engry_count, mean_score, mean_score_rmsd, d_rmsd


