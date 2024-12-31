# from caculate_score import *
from .muliti_chain_score import *
import os
from matplotlib import pyplot as plt
from Bio.PDB import *
import matplotlib.patches as mpl_patches
import glob

# def find_indx(seq):
#     ind_l = []
#     ind_r = []#对其后坐标对应的原始位置
#     cnt = 0
#     for i,s in enumerate(seq):
#         if s >= 'A' and s <= 'Z':
#             ind_l.append(i)
#             ind_r.append(cnt)
#             cnt = cnt + 1
#         else:
#             ind_r.append(-1)
#     return ind_l,ind_r

color_map = {'H': [237/255, 144/255, 144/255], 'G': [241/255, 177/255, 152/255], 'I': [240/255, 196/255, 216/255],
               'B': [214/255, 185/255, 124/255], 'E': [245/255, 239/255, 180/255], 'P': [181/255, 177/255, 209/255],
               'T': [133/255, 200/255, 189/255], 'S': [160/255,160/255,160/255], 'C': [210/255,210/255,210/255],
               'N': 'N'}
def plot_secondary(aa_ss, ind_l,line):
    ss_dict = {'H': 'H', 'G': 'G', 'I': 'I',
               'B': 'B', 'E': 'E', 'P': 'P',
               'T': 'T', 'S': 'S', 'C': 'C',
               'N': 'N'}

    ss_block = []
    prev_ss = None
    prev_in = -1
    for idx, com in enumerate(aa_ss):
        reduced_elem = ss_dict.get(com[1], 'C')
        if idx != 0 and idx % line != 0:
            if reduced_elem != prev_ss or idx != prev_in + 1:
                ss_block.append([reduced_elem, idx, idx])
                prev_ss = reduced_elem
            prev_in = idx
            ss_block[-1][-1] = idx
        elif idx == 0:
            if reduced_elem != prev_ss or idx != prev_in + 1:
                ss_block.append([reduced_elem, idx, idx])
                prev_ss = reduced_elem
            prev_in = idx
            ss_block[-1][-1] = idx
        else:
            end_idx = min(ind_l, idx)
            ss_block.append([reduced_elem, idx, end_idx])
            prev_ss = reduced_elem
            prev_in = idx
    return ss_block


def plot_fig1(ax, ss_block1, aa_ss1, aligned_seq1, aligned_seq2, energy_list, line, pad=0):
    fs = 9.4
    for i in range(len(aligned_seq2)):
        aa1 = aligned_seq1[i]
        aa2 = aligned_seq2[i]

        color = "black"  # 默认为黑色
        if aa1 != aa2:
            color = "#DC143C"  # 如果不同，字体颜色为红色
        # elif ss_type == "N":
        #     color = "lightgray"  # 如果ss_type为N，字体颜色为浅灰色

        ax.text((i % line) / line + 0.0005, 0.05 + (1 - ((i // line + 1)) * 0.2 - pad),
                aligned_seq1[i], size=fs, fontfamily="monospace", fontweight="bold",
                color=color)

    # 能量条
    s = 0
    for p in energy_list:
        if np.isnan(float(p)):
            color = 'white'  # 如果 p 是 NaN，将颜色设为白色
        else:
            p = float(p)
            color = plt.cm.Reds(p)
        # p = float(p)
        # color = plt.cm.Reds(p)
        # color.set_bad('black')

        ax.add_patch(
            mpl_patches.Rectangle(((s % line) / line - 0.001, 0.025 + (1 - ((s // line + 1)) * 0.2 - pad) - 0.025),
                                  1 / line + 0.001, 0.005, color=color))
        s += 1

    for m, n in enumerate(ss_block1):
        ss_type, start, end = n

        if ss_type == "C":
            ax.add_patch(
                mpl_patches.Rectangle(((start % line) / line - 0.001, 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                      (end - start + 1) / line + 0.001, 0.003, color=color_map["C"]))
            ax.text((i % line) / line, 0.072 + (1 - ((i // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((i % line) / line, 0.085 + (1 - ((i // line + 1)) * 0.2 - pad), str(i + 1), size=6, color="black")
        elif ss_type == "T":
            x = (start % line) / line
            y = 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)  # 调整y坐标位置
            width = (end - start + 1) / line - 0.0029
            height = 0.03

            # 计算半圆的半径和起始角度
            radius = width / 2
            start_angle = 0
            end_angle = 180

            # 绘制上弧形
            arc = mpl_patches.Arc((x + radius, y), width, height, angle=0, theta1=start_angle, theta2=end_angle,
                                  color=color_map["T"], linewidth=3)
            ax.add_patch(arc)
            ax.text((i % line) / line, 0.072 + (1 - ((i // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((i % line) / line, 0.085 + (1 - ((i // line + 1)) * 0.2 - pad), str(i + 1), size=6, color="black")
        elif ss_type == "S":
            ax.add_patch(
                mpl_patches.Rectangle(((start % line) / line - 0.001, 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                      (end - start + 1) / line + 0.001, 0.003, color=color_map['S']))

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")

        elif ss_type == "H":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['H'], scalex=False, scaley=False)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "G":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['G'], scalex=False, scaley=False)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "I":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['I'], scalex=False, scaley=False)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "P":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['P'], scalex=False, scaley=False)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "G":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['G'], scalex=False, scaley=False)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")

        elif ss_type == "E":
            rect = mpl_patches.Rectangle(((start % line) / line, 0.01 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                         (end - start + 1) / line - 0.0029, 0.03, linewidth=2, edgecolor=color_map['E'],
                                         facecolor=color_map['E'])
            ax.add_patch(rect)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "N":

            # 添加白色背景矩形，遮挡住之前的内容
            rect = mpl_patches.Rectangle(((start % line) / line - 0.001, 0.045 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                         (end - start + 1) / line + 0.0005, 0.017, color="white", zorder=9)
            ax.add_patch(rect)

            # 绘制灰色字体
            ax.text((start % line) / line + 0.0005, 0.05 + (1 - ((start // line + 1)) * 0.2 - pad),
                    " ".join(aligned_seq1[start:end + 1]) + " ", size=9.4, fontfamily="monospace", fontweight="bold",
                    color="#B3B6B5", zorder=10)
            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")



        elif ss_type == "B":

            rect = mpl_patches.Rectangle(((start % line) / line, 0.01 + (1 - ((start // line + 1)) * 0.2 - pad)),

                                         (end - start + 1) / line - 0.0029, 0.03, linewidth=2, edgecolor=color_map['B'],

                                         facecolor=color_map["B"])

            ax.add_patch(rect)

            ax.text((start % line) / line, 0.072 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")

            ax.text((start % line) / line, 0.085 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")

    ax.text(((ss_block1[-1][2] + 1) % line) / line + 0.005, 0.019 + (1 - ((ss_block1[-1][2] // line + 1)) * 0.2 - pad),
            "C loop", size=9.4, fontfamily="monospace", color="gray")
    ax.text(((ss_block1[-1][2]) % line) / line, 0.072 + (1 - ((ss_block1[-1][2] // line + 1)) * 0.2 - pad), "|", size=5,
            color="black")
    ax.text(((ss_block1[-1][2]) % line) / line, 0.085 + (1 - ((ss_block1[-1][2] // line + 1)) * 0.2 - pad),
            end + 1, size=6, color="black")

    ax.set_ylim(1 - (len(aa_ss1) / 25 + 4) * 0.1, 1.0)

    ax.axis("off")


def plot_fig2(ax, ss_block2, aa_ss2, aligned_seq2, aligned_seq1, line, pad=0.05):
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('top')
    fs = 9.4
    for i in range(len(aligned_seq1)):
        aa1 = aligned_seq1[i]
        aa2 = aligned_seq2[i]
        # print(ss_type)
        color = "#484e4f"  # 默认为黑色
        if aa1 != aa2:
            color = "red"  # 如果不同，字体颜色为红色

        ax.text((i % line) / line + 0.0005, -0.01 + (1 - ((i // line + 1)) * 0.2 - pad),
                aligned_seq2[i], size=fs, fontfamily="monospace", fontweight="bold", color=color)
    for m, n in enumerate(ss_block2):
        ss_type, start, end = n

        if ss_type == "C":

            ax.add_patch(
                mpl_patches.Rectangle(((start % line) / line - 0.001, 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                      (end - start + 1) / line + 0.001, 0.003, color=color_map['C']))

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "T":
            x = (start % line) / line
            y = 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)  # 调整y坐标位置
            width = (end - start + 1) / line - 0.0029
            height = 0.03

            # 计算半圆的半径和起始角度
            radius = width / 2
            start_angle = 0
            end_angle = 180

            # 绘制上弧形
            arc = mpl_patches.Arc((x + radius, y), width, height, angle=0, theta1=start_angle, theta2=end_angle,
                                  color=color_map['T'], linewidth=3)
            ax.add_patch(arc)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")


        elif ss_type == "S":

            ax.add_patch(
                mpl_patches.Rectangle(((start % line) / line - 0.001, 0.025 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                      (end - start + 1) / line + 0.001, 0.003, color=color_map['S']))

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "H":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['H'], scalex=False, scaley=False)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")

        elif ss_type == "G":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['G'], scalex=False, scaley=False)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "P":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['P'], scalex=False, scaley=False)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "I":
            n_turns = np.ceil((end - start + 1) / 1.5)
            x_val = np.linspace((start % line) / line + 0.0025, ((end + 0.95) % line) / line - 0.0025, 100)
            y_val = (1 - ((start // line + 1)) * 0.2 - pad) + 0.1 * (
                    -0.4 * np.sin(np.linspace(0, n_turns * 2 * np.pi, 100)) + 1) / 4
            ax.plot(x_val, y_val, linewidth=2.4, color=color_map['I'], scalex=False, scaley=False)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "E":
            rect = mpl_patches.Rectangle(((start % line) / line, 0.01 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                         (end - start + 1) / line - 0.0029, 0.03, linewidth=2, edgecolor=color_map['E'],
                                         facecolor=color_map['E'])
            ax.add_patch(rect)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "B":

            rect = mpl_patches.Rectangle(((start % line) / line, 0.01 + (1 - ((start // line + 1)) * 0.2 - pad)),

                                         (end - start + 1) / line - 0.0029, 0.03, linewidth=2, edgecolor=color_map['B'],

                                         facecolor=color_map['B'])

            ax.add_patch(rect)

            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")
        elif ss_type == "N":
            rect = mpl_patches.Rectangle(((start % line) / line - 0.001, -0.015 + (1 - ((start // line + 1)) * 0.2 - pad)),
                                         (end - start + 1) / line + 0.0005, 0.017, color="white", zorder=9)
            ax.add_patch(rect)

            # 绘制灰色字体

            ax.text((start % line) / line + 0.0005, -0.01 + (1 - ((start // line + 1)) * 0.2 - pad),
                    " ".join(aligned_seq2[start:end + 1]) + " ", size=fs, fontfamily="monospace", fontweight="bold",
                    color="#AEACAF", zorder=10)
            ax.text((start % line) / line, -0.025 + (1 - ((start // line + 1)) * 0.2 - pad), "|", size=5, color="black")
            ax.text((start % line) / line, -0.04 + (1 - ((start // line + 1)) * 0.2 - pad), start + 1, size=6, color="black")

    ax.text(((ss_block2[-1][2] + 1) % line) / line + 0.005, -0.01 + (1 - ((ss_block2[-1][2] // line + 1)) * 0.2 - pad),
            "C loop", size=fs, fontfamily="monospace", color="gray")
    ax.text(((ss_block2[-1][2]) % line) / line, -0.025 + (1 - ((ss_block2[-1][2] // line + 1)) * 0.2 - pad), "|", size=5,
            color="black")
    ax.text(((ss_block2[-1][2]) % line) / line, -0.04 + (1 - ((ss_block2[-1][2] // line + 1)) * 0.2 - pad),
            end + 1, size=6, color="black")

    ax.set_ylim(1 - (len(aa_ss2) / 25 + 4) * 0.1, 1)

    ax.axis("off")


def generate_and_save_structure_plot(name1, name2, pdb_file1, pdb_file2, dssp_file1, dssp_file2, save_folder, chainid1='ALL', chainid2='ALL'):#
    aligned_seq1, aligned_seq2, aligned_seq1_ss, aligned_seq2_ss, aligned_seq1_vector, aligned_seq2_vector, score_engry, score_engry_count, mean_score, mean_score_rmsd, d_rmsd = aligh_match(
        pdb_file1, name1, dssp_file1, pdb_file2, name2, dssp_file2, chainid1, chainid2 )
    VSS = 1 - (1 - mean_score / 4) ** 9
    SPS = 1 - (1 - mean_score_rmsd) ** 9
    cmap = plt.cm.Reds  # 使用红色调色板
    cmap.set_bad('white')  # 将NaN值设为黑色

    # 绘制热力图
    plt.matshow(d_rmsd, cmap=cmap, vmin=0, vmax=1)
    plt.gca().xaxis.set_ticks_position('bottom')
    # plt.matshow(d_rmsd, cmap=cmap)

    # 添加颜色条
    plt.colorbar()

    # 显示图形
    save_name1 = f"{save_folder}/{name1}_{chainid1}_{name2}_{chainid2}_SPS.png"
    plt.savefig(save_name1, dpi=300, bbox_inches='tight')
    # ind1, ind_r1 = find_indx(aligned_seq1)
    # ind2, ind_r2 = find_indx(aligned_seq2)
    aligned_seq1_ss = ["".join(item) if isinstance(item, tuple) else item for item in aligned_seq1_ss]

    aa_ss1 = list(zip(aligned_seq1, aligned_seq1_ss))
    aa_ss2 = list(zip(aligned_seq2, aligned_seq2_ss))

    # print(aligned_seq1_ss)
    # print(aa_ss1)
    end = len(aligned_seq1) - 1
    print(end)
    ss_block1 = plot_secondary(aa_ss1, end, line=80)
    ss_block2 = plot_secondary(aa_ss2, end, line=80)

    fig, ax = plt.subplots(figsize=(15, (end // 10) + 1))
    # fig, ax = plt.subplots()
    plot_fig1(ax, ss_block1, aa_ss1, aligned_seq1, aligned_seq2, score_engry, line=80, pad=0)
    plot_fig2(ax, ss_block2, aa_ss2, aligned_seq2, aligned_seq1, line=80, pad=0.05)
    # 调整图像大小
    # fig.set_size_inches(10, 300)  # 调整图像的宽度和高度
    save_name = f"{save_folder}/{name1}_{chainid1}_{name2}_{chainid2}_VSS.png"

    ax.text(-0.06, 0.85, name1, va='center', ha='center')
    ax.text(-0.06, 0.75, name2, va='center', ha='center')

    plt.savefig(save_name, bbox_inches='tight')
    plt.close()
    return VSS, SPS


if __name__ == '__main__':
    save_folder = r"F:\zhengly\code\result\3"
    save_folder1 = r"F:\zhengly\code\result\3"
    pdb_folder = r"F:\zhengly\code\data\pdb"
    dssp_folder = r"F:\zhengly\code\data\dssp"

    # data = pd.read_csv(r"F:\zhengly\code\data\test.csv")

    name1 = '6BYY'
    name2 = '6BZ1'

    pdb_file1 = os.path.join(pdb_folder, name1 + ".pdb")
    pdb_file2 = os.path.join(pdb_folder, name2 + ".pdb")
    dssp_file1 = os.path.join(dssp_folder, name1 + ".dssp")
    dssp_file2 = os.path.join(dssp_folder, name2 + ".dssp")

    generate_and_save_structure_plot(name1, name2, pdb_file1, pdb_file2, dssp_file1, dssp_file2, save_folder,
                                     save_folder1, chainid1=['A','B'], chainid2=['A','B'])

