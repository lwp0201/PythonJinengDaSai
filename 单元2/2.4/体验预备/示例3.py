import turtle        #导入turtle模块
x=100                #定义一个变量x，赋值为100
for i in range(4):
turtle.fd(x)         #前移x像素
turtle.left(90)      #左转90度              
turtle.done()        #停止绘画，保留绘图结果
