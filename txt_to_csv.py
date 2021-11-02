# 元素のMFのテキストデータを扱うプログラム。
# 元素の総MFと、Yi, Yeを計算する
import os
import pandas as pd
from config import *

# 詳細設定、PATH
header_names = ["Element", "Z", "A", "N", "mass[amu]", "solarMF", "MF", "IMF"]
DATA_PATH = PATH + "data/"
CSV_PATH = PATH + "csv/"
if not os.path.exists(CSV_PATH):
    os.makedirs(CSV_PATH)

FILE = PATH + "Ye_sumMF.txt"
if os.path.exists(FILE):
    os.remove(FILE)

f = open(FILE, "a")
for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                #------------------------------------------------------------------------------
                # 読み込むファイル名を指定
                TITLE = "last_Ye_" + x + "_T0_" + y + "_rho0_" + z
                INPUT_PATH = DATA_PATH + TITLE + ".txt"
                OUTPUT_PATH = CSV_PATH + TITLE + ".csv"

                if not os.path.exists(INPUT_PATH):
                    continue
                # テキストデータを読み込んで,csvファイルとして出力。
                read_text_file = pd.read_csv(INPUT_PATH, header = None, sep = "\t", names = header_names, encoding = "SHIFT-JIS")
                read_text_file.to_csv(OUTPUT_PATH, index = None)

                df = pd.read_csv(OUTPUT_PATH, header = 0)
                
                # print(df)
                # Yi, Ye の計算
                df['Yi'] = df["MF"] / df["mass[amu]"]
                df["Zi * Yi"] = df["Z"] * df["Yi"]
                df["Ni * Yi"] = df["N"] * df["Yi"]
                sum_ZiYi = df["Zi * Yi"].sum()
                sum_NiYi = df["Ni * Yi"].sum()
                # print("sum_ZiYi : %.10f, sum_NiYi : %.10f" % (sum_ZiYi, sum_NiYi))
                sum_Ye = sum_ZiYi / (sum_ZiYi + sum_NiYi)
                # print(sum_Ye)
                # MF の計算
                sum_MF = df["MF"].sum()
                # # print("sum_MF : %.10f" % sum_MF)
                print("%s, Ye : %.10f" % (TITLE, sum_Ye))
                f.write("%s  %s  %s  %s  %.10f  %.10f\n" % (w, x, y, z, sum_Ye, sum_MF))
