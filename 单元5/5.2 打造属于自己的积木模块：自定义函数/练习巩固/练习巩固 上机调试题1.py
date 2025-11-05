'''
编写自定义函数，实现输入梯形的上底、下底和高，计算出梯形的面积
'''
import random


def get_s(top,bottom,height):
    s=(top+bottom)*height/2
    return s
while True:
    top=int(input("请输入梯形的上底："))
    bottom=int(input("请输入梯形的下底："))
    height=int(input("请输入梯形的高："))
    print("梯形的面积为{}".format(get_s(top,bottom,height)))