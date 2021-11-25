"""
##      crop.py
##      version 1
##      python --version : 3.6.13
##      cv2.__version__ : 4.5.4-dev
##      emailremoved@ ( ozan.akyel54@gmail.com )
##      @author : Ozan AKYEL

"""
import cv2
import os

i=1
image_folder = 'C:/Users/ozan.akyel/Desktop/project 2021/siperlik toka/raw_datas/tip2_raw/'     # source of reading image folder
save_folder = 'C:/Users/ozan.akyel/Desktop/project 2021/siperlik toka/raw_datas/tip2_raw_crop'        # save folder (target)
def crop(name):
    image = cv2.imread(image_folder+name)
    name, ext = name.split('.')                                             # resim isminden .jpg ayrılıyor
    print(f"{name} resim okundu")
    y_min = 650  # y yatay
    x_min = 600  # x dikey
    y_max = 1050
    x_max = 900
    crop_image = image[x_min:x_max, y_min:y_max]
    # cv2.imshow("Cropped", crop_image)
    print(crop_image.shape)
    # cv2.waitKey(0)
    # saving = os.path.join(save_folder, f"{name}_crop.jpg")                # kayıt işleminde faklılık için kullanılabilir
    cv2.imwrite(os.path.join(save_folder, f"{name}_crop.jpg"), crop_image)
    print(f"folder = {save_folder} #### {name}_crop.jpg olarak kaydedildi")


for img in os.listdir(image_folder):                                        # os ile klasör altındaki tüm dosyalar listelenir
    if img.endswith('.jpg'):
        crop(img)
        i+=1
        print(i)
    else:
        print(img + 'bir .jpg dosyası degil')
