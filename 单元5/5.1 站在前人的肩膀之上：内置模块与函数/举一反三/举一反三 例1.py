"""
🏥 ================================================
    内置模块应用 - BMI健康指数计算器
================================================

📝 功能说明：
    使用Python内置random模块随机生成身高体重数据
    计算BMI指数并根据中国标准评估健康状况
    展示了内置模块在实际应用中的强大功能

🔧 主要知识点：
    • random模块的使用 (random.uniform)
    • 数学计算和公式应用 (BMI = weight/height²)
    • 条件判断语句 (if-elif-else)
    • 无限循环控制 (while True)
    • 字符串格式化输出 (.format)
    • 用户交互控制 (input)

🎯 学习目标：
    掌握random模块的基本用法
    理解数学计算在编程中的应用
    学会使用条件判断进行数据分类
    掌握用户交互和程序控制

💡 扩展思考：
    可以添加更多健康指标计算
    可以保存历史数据进行分析
    可以添加图形化界面显示结果
    可以集成到健康管理系统中

📊 BMI标准参考：
    • BMI < 18.5：体重过低
    • 18.5 ≤ BMI < 24：体重正常  
    • 24 ≤ BMI < 28：超重
    • BMI ≥ 28：肥胖
"""

import random
while True:
    msg = ""
    height = random.uniform(1.6, 1.8)       # 身高在1米6到1米8之间
    weight = random.uniform(50, 80)         # 体重要求在50公斤到80公斤之间
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        msg ="体重过低"
    elif 18.5 <= bmi < 24:
        msg="体重正常"
    elif 24 <= bmi < 28:
        msg="超重"
    else:
        msg="肥胖"
    print("身高：{:.1f}米，体重：{:.1f}公斤".format(height,weight))
    print("BMI指数：{:.2f} (kg/m^2)".format(bmi))
    print("身体状况：{}".format(msg))
    input()