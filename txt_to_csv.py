# 元素のMFのテキストデータを扱うプログラム。
# 元素の総MFと、Yi, Yeを計算する
print("run 'txt_to_csv.py'")

# ------------------------------------------------------------------------------------------------------------------------------
import os
import pandas as pd
from config import *

# ------------------------------------------------------------------------------------------------------------------------------
# 詳細設定、PATH
header_names = ["Element", "Z", "A", "N", "mass[amu]", "solarMF", "MF", "IMF"]
DATA_PATH = PATH + "data/"
RESULT_PATH = PATH + "result/"
CSV_PATH = PATH + "csv/"

if not os.path.exists(CSV_PATH):
    os.makedirs(CSV_PATH)

if not os.path.exists(RESULT_PATH):
    os.makedirs(RESULT_PATH)

FILE1 = RESULT_PATH + "Ye_sumMF.txt"
if os.path.exists(FILE1):
    os.remove(FILE1)


FILE2 = RESULT_PATH + "sum_MF_larger_1.txt"
if os.path.exists(FILE2):
    os.remove(FILE2)

# ------------------------------------------------------------------------------------------------------------------------------
# 実行
f1 = open(FILE1, "w")
f2 = open(FILE2, "w")
for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                #------------------------------------------------------------------------------
                # 読み込むファイル名を指定
                TI = "Ye_" + x + "_T0_" + y + "_rho0_" + z
                TITLE = w + "_" + TI

                INPUT_PATH = DATA_PATH + TITLE + ".txt"
                OUTPUT_PATH = CSV_PATH + TITLE + ".csv"

                if not os.path.exists(INPUT_PATH):
                    continue
                if os.path.exists(OUTPUT_PATH):
                    continue
                #------------------------------------------------------------------------------
                # テキストデータを読み込んで,csvファイルとして出力。
                read_text_file = pd.read_csv(INPUT_PATH, header = None, sep = "\t", names = header_names, encoding = "SHIFT-JIS")
                read_text_file.to_csv(OUTPUT_PATH, index = None)

                #------------------------------------------------------------------------------
                # csvファイルを読み込んで計算
                df = pd.read_csv(OUTPUT_PATH, header = 0)
                
                # Yi, Ye の計算
                df['Yi'] = df["MF"] / df["mass[amu]"]
                df["Zi * Yi"] = df["Z"] * df["Yi"]
                df["Ni * Yi"] = df["N"] * df["Yi"]
                sum_ZiYi = df["Zi * Yi"].sum()
                sum_NiYi = df["Ni * Yi"].sum()
                sum_Ye = 0
                if sum_ZiYi + sum_NiYi != 0:
                    sum_Ye = sum_ZiYi / (sum_ZiYi + sum_NiYi)
                
                # MF の計算
                sum_MF = df["MF"].sum()
                #------------------------------------------------------------------------------
                # OUTPUT

                if sum_MF >= 1.1:
                    f2.write("%s\n" % TI)

                f1.write("%s  %s  %s  %s  %.10f  %.10f\n" % (w, x, y, z, sum_Ye, sum_MF))
