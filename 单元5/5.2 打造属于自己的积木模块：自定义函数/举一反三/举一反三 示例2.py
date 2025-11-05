'''
1.几何立体的意义
2.
计算圆柱体的底面积，圆柱体，输入底面半径，圆柱体
'''
import math
def get_dmj(r):
    return math.pi*r**2
def get_tj(s,h):
    return s*h

while True:
    r=int(input("请输入半径r的值："))
    h=int(input("请输入高h的值："))
    dmj=get_dmj(r)
    print("底面半径为{}的圆柱体底面积是{:.2f}".format(r,dmj))
    tj=get_tj(dmj,h)
    print("底面半径为{},高为{}的圆柱体体积是{:.2f}".format(r,h,tj))