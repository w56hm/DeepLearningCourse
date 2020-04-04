import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("lena.tiff")
img_r,img_g,img_b=img.split()
plt.figure(figsize=(20,20))
plt.rcParams["font.sans-serif"]="SimHei"

plt.subplot(221)
plt.axis("off")
Ima_r=img_r.resize(50,50)
plt.imshow(Ima_r,cmap='gray')
plt.title("R-缩放",fontsize=14)


plt.subplot(222)
Ima_g=img_g.transpose(Image.FLIP_LEFT_RIGHT)
i_g=img_g.transpose(Image.ROTATE_270)
plt.imshow(i_g,cmap='gray')
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
Ima_b=img_b.crop(0,0,150,150)
plt.imshow(Ima_b,cmap='gray')
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
plt.axis("off")
img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb,cmap='gray')
plt.title("R-缩放",fontsize=14)

img_rgb.save("test.png")


plt.suptitle("图像基本操作",fontsize=20,color="b") 
plt.show( )


