# coding:utf-8
import os
from PIL import Image

# author :香菜
# 製作gif
imgFolderPath = "D:\\gif"
fileList = os.listdir(imgFolderPath)
firstImgPath = os.path.join(imgFolderPath, fileList[0])
im = Image.open(firstImgPath)
images = []
for img in fileList[1:]:
   imgPath = os.path.join(imgFolderPath, img)
   images.append(Image.open(imgPath))
im.save('beauty.gif', save_all=True,append_images =images,loop = 0,duration=2000)