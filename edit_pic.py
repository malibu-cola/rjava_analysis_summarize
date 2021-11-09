# r-javaのスクリーンショットをトリミングするコード
print("run 'edit_pic.py'")

# ------------------------------------------------------------------------------------------------------------------------------
from PIL import Image
import os
from posixpath import normcase
from config import *

# ------------------------------------------------------------------------------------------------------------------------------
# PATH の指定
PIC_PATH = PATH + "pic/"
PICEDIT_PATH = PATH + "pic_edit/"

if not os.path.exists(PICEDIT_PATH):
    os.makedirs(PICEDIT_PATH)

# ------------------------------------------------------------------------------------------------------------------------------
# 実行
for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                # 読み込むファイル名を指定
                TI = "Ye_"+ x + "_T0_" + y + "_rho0_" + z
                TITLE = w + "_" + TI
                
                # 読み込むファイルの相対パス
                INPUT_PATH = PIC_PATH + TITLE + ".png"
                OUTPUT_PATH = PICEDIT_PATH + TITLE + ".png"

                # 読み込むファイルが存在しなければ、飛ばす。
                if not os.path.exists(INPUT_PATH):
                    continue
                # 既に編集済みならば飛ばす。
                if os.path.exists(OUTPUT_PATH):
                    continue

                # ファイルを読み込む
                cat = Image.open(INPUT_PATH)
                # 画像を切り抜く（左上のx, 左上のy, 右下のx, 右下のy）
                crop_cat = cat.crop((140, 250, 1300, 940))
                # 切り抜いた画像を保存
                crop_cat.save(OUTPUT_PATH)
