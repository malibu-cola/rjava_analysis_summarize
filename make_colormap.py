# 温度を縦軸、密度を横軸にとり、存在量を色分けしてウランなどの存在量マップを作るためのコード
print ("run 'make_colormap.py'")

# ------------------------------------------------------------------------------------------------------------------------------
import os
import glob
import linecache
from posixpath import normcase
from matplotlib.colors import LogNorm
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from config import *

# ------------------------------------------------------------------------------------------------------------------------------
# PATH の指定
DATA_PATH = PATH + "data/"
sumMF_PATH = PATH + "result/sum_MF_larger_1.txt"
CNT100_PATH = PATH + "result/cnt_larger_100.txt"
COLORMAP_PATH = PATH + "result/colormap/"
CLMP_Th232_PATH = COLORMAP_PATH + "Thorium232/"

if not os.path.exists(CLMP_Th232_PATH):
    os.makedirs(CLMP_Th232_PATH)

g = open(sumMF_PATH, "r")
DATALIST = g.readlines()

g2 = open(CNT100_PATH, "r")
DATALIST2 = g.readlines()
# ------------------------------------------------------------------------------------------------------------------------------
# colormapを作成

# ------------------------------------------------------------------------------------------------------------------------------
# テキストファイルからウラン238のMFを読み込み、配列に入れていく
m = 0
n = 0
for x in Ye:

    # ( T の個数) * ( rho の個数) だけの配列を準備
    graph = [[0,0,0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0],\
                            [0,0,0,0,0,0,0,0,0,0,0],\
                                [0,0,0,0,0,0,0,0,0,0,0],\
                                    [0,0,0,0,0,0,0,0,0,0,0]]
    # 参照する行を初期化
    n = 0

    for y in T0:
        # 参照する列を初期化
        m = 0

        for z in rho0:
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # 読み込むファイルの相対パス
            TI = "Ye_"+ x + "_T0_" + y + "_rho0_" + z
            TITLE = "last_" + TI
            INPUT_PATH = DATA_PATH + TITLE + ".txt"
            # print("TI : %s" % TI)

            # もしパスが存在しなかったら参照する配列は次の列に進む。
            if not os.path.exists(INPUT_PATH):
                graph[n][m] = None
                m += 1
                continue
            
            # sum_MF >= 1 のパスを読み込んでスキップ
            ok = True
            for g_line in DATALIST:
                if TI + "\n" == g_line:
                    ok = False
            if not ok:
                graph[n][m] = 1000
                m += 1
                continue

            # cntMAX >= 100 のところを飛ばす。
            ok = True
            for g_line2 in DATALIST2:
                if TI + "\n" == g_line2:
                    ok = False
            if not ok:
                graph[n][m] = 1000
                m += 1
                continue
            

            
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # 読み込む元素の行を指定し、空白で分割する。
            TARGET_LINE = linecache.getline(INPUT_PATH,5911) # Th232:5911, U235:6123,  Uran238:6126, 
            element, Z, A, N, mass, solarMF, MF,InitialMF = TARGET_LINE.split()

            # MassFraction が0だったら1e-100に治す。
            if MF == "0.0":
                MF = '0.000000000000000000000000000000000000000000000000001' #1e-100

            # MassFraction がNaN(計算不能)であれば、参照する配列をNaneにし、次の列に進む。
            if MF == "NaN":
                graph[n][m] = None
                m += 1
                continue

            # 参照する配列に MF を代入する。
            graph[n][m] = float(MF)
            linecache.clearcache() # キャッシュをクリア

            # 参照する列を次に進める。
            m+=1

        # 参照する行を次に進める。
        n += 1
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 各 Yeごとにcolormapを作成する。
    # colormapの目盛りを指定。
    df = pd.DataFrame(data = graph, \
        index = ["T_4e9", "T_7e9",\
            "T_1e10", "T_4e10", "T_7e10", \
                "T_1e11", "T_4e11", "T_7e11", \
                    "T_1e12"], \
        columns = ["rho_1e10", "rho_4e10", "rho_7e10", \
            "rho_1e11", "rho_4e11", "rho_7e11",\
                "rho_1e12","rho_4e12","rho_7e12",\
                    "rho_1e13","rho_4e13"])
    
    # 図を描画
    plt.figure()
    sns.heatmap(df, annot=False, norm = LogNorm(), vmax = 1.0, vmin = 1e-20)

    # 図のタイトル
    FIG_TITLE = "last_Thorium232_Ye_" + x
    # FIG_TITLE = "last_Uranium235_Ye_" + x
    # FIG_TITLE = "last_Uranium238_Ye_" + x

    # タイトルを描画
    plt.title("%s" % FIG_TITLE)

    # 図を保存
    plt.savefig(CLMP_Th232_PATH + FIG_TITLE + ".png")# 保存場所
    # plt.savefig(PATH + "result/colormap/Uranium235/" + FIG_TITLE + ".png")# 保存場所
    # plt.savefig(PATH + "result/colormap/Uranium238/" + FIG_TITLE + "2.png")# 保存場所

    # 図を閉じる。
    plt.close('all')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------