import numpy as np
np.random.seed(612)
ran=np.random.rand(1000)
a = int(input("请任意输入一个1到100的数："))
m=0
for i in range(1000):
   if i%a==0:
       print(m+1,i,ran[i])
       m=m+1
      
