import cv2
import time
import glob
import os
import random

# 設定
mosaic_deg = 0.01
interval   = 5

# クイズ作成
list = glob.glob('images/*.png')
data = random.choice(list)
quiz = os.path.split(data)[1]

def mosaic(file, scale):
    # 元ファイル
    fname = file
    img = cv2.imread(fname) 

    img_height,img_width=img.shape[:2]  

    scale_factor = scale
    img = cv2.resize(img,None,fx=scale_factor,fy=scale_factor)
    img = cv2.resize(img, (img_width, img_height),interpolation=cv2.INTER_NEAREST)

    cv2.imwrite('mosaic.png',img)

# タイトルコール

# 答え
print(quiz)
time.sleep(2)
# 答え隠し
print('-\n\n\n\n\n\n')
time.sleep(2)
for _ in range(15):
    mosaic('images/' + quiz, mosaic_deg)
    time.sleep(interval)
    mosaic_deg += 0.01
