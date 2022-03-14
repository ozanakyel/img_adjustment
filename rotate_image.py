"""
##      rotate_image.py
##      version 1
##      python --version : 3.6.13
##      emailremoved@ ( ozan.akyel54@gmail.com )
##      @author : Ozan AKYEL
"""

from cv2 import cv2
import os
from scipy import ndimage

saving_path = r"C:\Users/Saving_path"
image_folder = r'C:\Users/image_source_folder_path'
angle = -25
if not os.path.exists(saving_path): # if saving folder isn't exists, will be creating
    try:
        os.makedirs(saving_path)
        print(f"{saving_path} was created")
    except FileExistsError:
        print("can not created")
else:
    print("Directory " , saving_path ,  " already exists")

def image_rotate(img, angle, scale = 1):
    h,w,c =img.shape
    center = (h/2, w/2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    final_rotated = cv2.warpAffine(img, rotation_matrix, (w, h))
    return final_rotated


for img in os.listdir(image_folder):
    if img.endswith('.jpg'):
        print(img)
        image = cv2.imread(os.path.join(image_folder, img))
        name, ext = img.split('.')
        print("name :", name)
        rotated_img = image_rotate(image, angle)

        # rotated_img = cv2.resize(rotated_img, (800, 800))                   # optional to preview
        # cv2.imshow("rotated", rotated_img)
        # cv2.waitKey(0)

        # saving = os.path.join(save_folder, f"{name}_crop.jpg")                # to custom saving
        cv2.imwrite(os.path.join(saving_path, f"{name}_rotated.jpg"), rotated_img)
        print(f"folder = {saving_path} #### {name}_crop.jpg olarak kaydedildi")

    else:
        print(img + ' It is not a .jpg file')