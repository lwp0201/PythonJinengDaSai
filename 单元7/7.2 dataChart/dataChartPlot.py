
import matplotlib.pyplot as plt
import pandas as pd

# 读取CSV文件
csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.2 dataChart\示例名单.csv'  # CSV文件路径
getGender = []  # 初始化存储性别的列表
df = pd.read_csv(csvFilePath,encoding='utf-8')
#求三个评委的平均分，并且保留2位小数。
df['平均分']=df[['评委1','评委2','评委3']].mean(axis=1).round(2)

#绘制折线图
plt.plot(df['姓名'], df['平均分'], marker='o')
plt.rcParams['font.sans-serif']=['SimHei'] #设置中文字体
plt.xticks(rotation=-90)            #x轴文字反转90度
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.title("端午包粽子参赛学生成绩记录折线图")
# 添加数据标签
for i, score in enumerate(df['平均分']):
    plt.text(i, score, f'{score}', ha='center', va='bottom')

plt.grid(True)
plt.savefig('端午包粽子参赛学生成绩记录折线图.png')  # 保存图表为png文件
plt.show()