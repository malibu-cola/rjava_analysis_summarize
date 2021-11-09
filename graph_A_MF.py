# 質量数A に対する MF のグラフを csv から出力するプログラム
print("run 'graph_A_MF.py'")

# ------------------------------------------------------------------------------------------------------------------------------
import os
import pandas as pd
import matplotlib.pyplot as plt
from config import *
# import nampy as np

CSV_PATH = PATH + "csv/"
OUTPUT_PATH = PATH + "result/FIG_A_MF/"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                TITLE = w + "_Ye_" + x + "_T0_" + y + "_rho0_" + z
                # print(TITLE)
                INPUT_FILE = CSV_PATH + TITLE + ".csv"
                OUTPUT_FILE = OUTPUT_PATH + TITLE + ".png"

                if not os.path.exists(INPUT_FILE):
                    continue

                dt = pd.read_csv(INPUT_FILE)
                # print(dt)

                fig = dt.plot(x = "A", y = "MF")
                plt.yscale("log")
                plt.xlim([0,300])
                plt.ylim([1e-15,1])
                # plt.show()
                fig.get_figure().savefig(OUTPUT_FILE)
                plt.close()