# colormap を作成する際に、指定のディレクトリ名、ファイル名ではない際に、まとめて名前を変更するためのコード。

import os
import glob
from config import *

for x in Ye:
    for y in T:
        for z in rho:
            # 変更前の相対パスとファイル名
            pre_PATH = PATH + pic + "Ye_" + x + "/" +  
            exist = os.path.exists(path)
            if not exist:
                continue
            # 変更後の相対パスとファイル名
            path2 = "../../progress/1018to1025/pic/Ye_009/NSE_Ye_" + x + "_T0_" + y + "_rho0_" + z + ".png"
            os.rename(path,path2)