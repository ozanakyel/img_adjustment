import os.path
from cv2 import cv2
import os

i=1
image_folder = 'C:/Users/ozan.akyel/Desktop/toka_rev2/yeni_tipler/'     # resimlerin okunacağı klasör
save_folder = 'C:/Users/ozan.akyel/Desktop/toka_rev2/deneme/'        # kaydedilecek klasör
def resizer(name):
    image = cv2.imread(image_folder+name)
    name, ext = name.split('.')                                             # resim isminden .jpg ayrılıyor
    resize_image = cv2.resize(image, (640,640))
    cv2.imshow(name, resize_image)
    print(resize_image.shape)
    cv2.waitKey(0)
    # saving = os.path.join(save_folder, f"{name}_crop.jpg")                # kayıt işleminde faklılık için kullanılabilir
    # cv2.imwrite(os.path.join(save_folder, f"{name}_crop.jpg"), resize_image)
    print(f"folder = {save_folder} #### {name}_crop.jpg olarak kaydedildi")


for img in os.listdir(image_folder):                                        # os ile klasör altındaki tüm dosyalar listelenir
    if img.endswith('.jpg'):
        resizer(img)
        i+=1
        print(i)
    else:
        print(img + 'bir .jpg dosyası degil')