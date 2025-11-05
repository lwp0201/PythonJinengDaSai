'''
将下列代码输入到计算机中，运行并观察输出的结果，理解该代码的含义
并说说draw_graph中的n有什么作用
'''
import turtle as t
def draw_graph(n):
    for i in range(n):
        t.fd(90)
        t.left(360/n)

def draw_goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

draw_graph(4)
draw_goto(100,100)
draw_graph(5)
draw_goto(-200,-200)
draw_graph(7)
t.done()
'''
知识点：
1.讲解as  #
2.自定义函数的参数
'''