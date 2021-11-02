from matplotlib.pyplot import colormaps
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.util import Cm, Pt
import os
from posixpath import normcase
from config import *

PIC_EDIT_PATH = PATH + "pic_edit/"
COLORMAP_PATH = PATH + "result/colormap/"
OUTPUT_PATH = PATH + "result/pic_pptx/"
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
for w in status:

    for x in Ye:
        n = 0
        # -----------------------------------------------------------------------
        # Presentation オブジェクトを生成
        ppt = Presentation()

        # スライドのサイズを指定
        ppt.slide_width = Cm(33.868)
        ppt.slide_heght = Cm(19.05)

        # ----------------------------------------------------------------------
        # スライド1枚目
        # 追加するスライドを選択
        slide_layout_0 = ppt.slide_layouts[0]
        # スライドを追加
        slide_0 = ppt.slides.add_slide(slide_layout_0)
        # place holder (テキスト入れるやつ？)を選択
        slide_0_title = slide_0.placeholders[0]
        # スライドに貼り付け
        print(type(slide_0_title))
        # スライドの幅
        slide_0_title.width = Cm(30)
        # スライドの高さ
        slide_0_title.height = Cm(20)
        # スライドの文字
        slide_0_title.text = "result picture"

        # ----------------------------------------------------------------------
        # スライド2枚目
        # 追加するスライドを選択
        slide_layout_0 = ppt.slide_layouts[0]
        # スライドを追加
        slide_0 = ppt.slides.add_slide(slide_layout_0)
        # place holder (テキスト入れるやつ？)を選択
        slide_0_title = slide_0.placeholders[0]
        # スライドに貼り付け
        print(type(slide_0_title))
        # スライドの幅
        slide_0_title.width = Cm(30)
        # スライドの高さ
        slide_0_title.height = Cm(20)
        # スライドの文字
        slide_0_title.text = "Ye:" + x
        # ----------------------------------------------------------------------
        for y in T0:
            m = 0
            for z in rho0:
                # ----------------------------------------------------------------------
                # スライド3枚目以降 (それぞれの条件でのcolormapとスクショ)
                #
                picname = w + "_Ye_" + x + "_T0_" + y + "_rho0_" + z + ".png"
                input_pic_path = PIC_EDIT_PATH + picname
                
                if not os.path.exists(input_pic_path):
                    m += 1
                    continue

                # スライドのレイアウトを選択
                slide_layout_6 = ppt.slide_layouts[6]
                # スライドを追加
                slide_6 = ppt.slides.add_slide(slide_layout_6)

                # 画像のplaceholder を作成
                shapes = slide_6.shapes
                shapes.add_picture(input_pic_path, Cm(15), Cm(3), width = None, height = Cm(10.88))
                colormap_path = COLORMAP_PATH + "Thorium232/last_Thorium232_Ye_" + x + ".png"
                shapes.add_picture(colormap_path, 0, Cm(3), width = None, height = Cm(10.88))

                # 指定する長方形を追加
                rect0 = slide_6.shapes.add_shape(
                    MSO_SHAPE.RECTANGLE,
                    Pt(52 + 23 * m), Pt(122 + 26 * n),
                    Pt(22), Pt(26)
                )
                rect0.fill.background()
                rect0.line.width = Pt(2)

                # # placeholder_1 = slide_6.placeholders[1]
                shape = shapes.add_textbox(Cm(20), Cm(14), Cm(22), Cm(16))
                # # box内にテキストを追加
                shape.text = picname

                shape1 = shapes.add_textbox(Cm(2), Cm(14),Cm(4), Cm(16))
                shape1.text = "Ye : "
                
                shape2 = shapes.add_textbox(Cm(2), Cm(16),Cm(4), Cm(18))
                shape2.text = "sum_MF : "
                
                shape3 = shapes.add_textbox(Cm(2), Cm(18),Cm(4), Cm(20))
                shape3.text = "Information : "

                # ----------------------------------------------------------------------
                m += 1
            n += 1
            # スライドのレイアウトを選択
            slide_layout_6 = ppt.slide_layouts[6]
            # スライドを追加
            slide_6 = ppt.slides.add_slide(slide_layout_6)

        # 保存  
        ppt.save(OUTPUT_PATH + w + "_Ye_"+ x + ".pptx")