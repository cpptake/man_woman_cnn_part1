import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from PIL import Image
#%matplotlib inline

#入力ファイルのパスを指定
in_img_man = "./rowdata/man/"
in_img_woman = "./rowdata/woman/"
out_img_man = "/facedata/man/"
out_img_woman = "/facedata/woman/"
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"


#画像データのリストを取得
in_man_files = os.listdir(in_img_man)
in_woman_files= os.listdir(in_img_woman)

def make_mydir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def face_detector(image_dir, image_files, save_dir, cascade_path):
#    for i in pic:
    for i in len(image_files):
        image_path = os.path.join(image_dir, im)
        print(image_path)

        # 画像の読み込み
        image_gs = cv2.imread(image_dir)
        # 顔認識用特徴量ファイルを読み込む --- （カスケードファイルのパスを指定）
        cascade = cv2.CascadeClassifier(cascade_path)
        # 顔認識の実行
        facerect = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=3, minSize=(1, 1))

        # 顔だけ切り出して保存
        i_faces  = 1
        if len(facerect) > 0:
            for rect in facerect:
                x = rect[0]
                y = rect[1]
                width = rect[2]
                height = rect[3]
                dst = image_gs[y:y + height, x:x + width]
                save_path = os.path.join(save_dir, out_file)
                #save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '.jpg'
                print(save_path)
                cv2.imwrite(save_path, dst)

                i_faces += 1


            else:
                print("No faces detected.")
                continue
            print("done...")

#in_img_man,in_img_woman,out_img_man,out_img_woman,cascade_path

face_detector(in_img_man, in_man_files, out_img_man, cascade_path)
face_detector(in_img_woman, in_woman_files, out_img_woman, cascade_path)
