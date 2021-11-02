from PIL import Image
import os
from posixpath import normcase
from config import *

OUTPUT_PATH = PATH + "pic_edit/"
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

for w in status:
    for x in Ye:
        for y in T0:
            for z in rho0:
                # 読み込むファイル名を指定
                INPUT_FILE = w + "_Ye_" + x + "_T0_" + y + "_rho0_" + z + ".png"
                # 読み込むファイルの相対パス
                INPUT_PATH = PATH + "pic/" + INPUT_FILE
                OUTPUT_FILE = OUTPUT_PATH + INPUT_FILE
                # 読み込むファイルが存在しなければ、飛ばす。
                if not os.path.exists(INPUT_PATH):
                    # print("%s : fly" % INPUT_PATH)
                    continue
                # 既に編集済みならば飛ばす。
                if os.path.exists(OUTPUT_FILE):
                    continue
                print(INPUT_PATH)
                # ファイルを読み込む
                cat = Image.open(INPUT_PATH)
                # 画像を切り抜く（左上のx, 左上のy, 右下のx, 右下のy）
                crop_cat = cat.crop((140, 250, 1300, 940))
                # 切り抜いた画像を保存
                crop_cat.save(OUTPUT_FILE)
