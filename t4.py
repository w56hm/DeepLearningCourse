import numpy as ny
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']="SimHei"

x=ny.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
y=ny.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
plt.scatter(x,y,color="red",marker="o")
plt.title("商品房销售记录",fontsize="16",color="b")
plt.xlabel("面积(平方米)",fontsize="14")
plt.ylabel("价格(万元)",fontsize="14")

plt.show()