import math
print("求解一元二次方程ax²+bx+c")
a=float(input("请输入a："))
b=float(input("请输入b："))
c=float(input("请输入c："))
d=b**2-4*a*c
if d>0:
    x1 = ((-b + math.sqrt(d)) // (2 * a))
    x2 = ((-b - math.sqrt(d)) // (2 * a))
    print("x1=", x1, "\t", "x2", x2)
elif d<0:
    print("无解")
else:
    print("一个解：")
    x1 = ((-b - math.sqrt(d)) // (2 * a))
    print("x1=x2=", x1)


