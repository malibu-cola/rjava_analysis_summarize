print("run 'read_INFODATA.py'")
from config import *
import os
DATA_PATH = PATH + "data/"
FILE2 = PATH + "result/cnt_larger_100.txt"
f2 = open(FILE2, "w")

for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                TI = "Ye_" + x + "_T0_" + y + "_rho0_" + z
                TITLE = w + "_" + TI

                cnt = 0
                cntMAX = 0
                if w == "last":
                    for i in range(101):
                        INFORMATION_PATH = DATA_PATH + "InformationData_" + TI + "_cnt_" + str(cnt) + ".txt"
                        if os.path.exists(INFORMATION_PATH):
                            cntMAX = max(int(cntMAX), int(cnt))
                        cnt += 1
                    if cntMAX >= 100:
                        # print("cnt100 : %s" % TITLE)
                        f2.write("%s\n" % TITLE)
