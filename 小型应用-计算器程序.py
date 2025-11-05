# 小型应用-计算器程序
'''
题目: 开发一个功能完整的计算器程序
要求掌握小型应用项目程序的开发方法

功能包括：
1. 基本四则运算
2. 科学计算功能
3. 历史记录
4. 表达式计算
5. 错误处理
6. 用户界面
'''

import math
import re
import json
import os
from datetime import datetime

class Calculator:
    def __init__(self):
        """
        初始化计算器
        """
        self.history = []
        self.history_file = "calculator_history.json"
        self.load_history()
    
    def load_history(self):
        """
        加载历史记录
        """
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
            except Exception as e:
                print(f"加载历史记录失败：{e}")
                self.history = []
    
    def save_history(self):
        """
        保存历史记录
        """
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存历史记录失败：{e}")
    
    def add_to_history(self, expression, result):
        """
        添加计算记录到历史
        """
        record = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'expression': expression,
            'result': result
        }
        self.history.append(record)
        
        # 只保留最近100条记录
        if len(self.history) > 100:
            self.history = self.history[-100:]
        
        self.save_history()
    
    def basic_calculate(self, a, operator, b):
        """
        基本四则运算
        """
        try:
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '*':
                return a * b
            elif operator == '/':
                if b == 0:
                    raise ValueError("除数不能为零")
                return a / b
            elif operator == '**':
                return a ** b
            elif operator == '%':
                return a % b
            else:
                raise ValueError(f"不支持的运算符：{operator}")
        except Exception as e:
            raise ValueError(f"计算错误：{e}")
    
    def scientific_calculate(self, func, value):
        """
        科学计算函数
        """
        try:
            if func == 'sin':
                return math.sin(math.radians(value))
            elif func == 'cos':
                return math.cos(math.radians(value))
            elif func == 'tan':
                return math.tan(math.radians(value))
            elif func == 'asin':
                return math.degrees(math.asin(value))
            elif func == 'acos':
                return math.degrees(math.acos(value))
            elif func == 'atan':
                return math.degrees(math.atan(value))
            elif func == 'log':
                if value <= 0:
                    raise ValueError("对数的真数必须大于0")
                return math.log10(value)
            elif func == 'ln':
                if value <= 0:
                    raise ValueError("对数的真数必须大于0")
                return math.log(value)
            elif func == 'sqrt':
                if value < 0:
                    raise ValueError("负数不能开平方根")
                return math.sqrt(value)
            elif func == 'factorial':
                if value < 0 or value != int(value):
                    raise ValueError("阶乘只能计算非负整数")
                return math.factorial(int(value))
            elif func == 'abs':
                return abs(value)
            elif func == 'ceil':
                return math.ceil(value)
            elif func == 'floor':
                return math.floor(value)
            else:
                raise ValueError(f"不支持的函数：{func}")
        except Exception as e:
            raise ValueError(f"科学计算错误：{e}")
    
    def evaluate_expression(self, expression):
        """
        计算表达式
        """
        try:
            # 预处理表达式
            expression = expression.replace(' ', '')
            
            # 替换一些常见的数学函数
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('e', str(math.e))
            
            # 处理科学计算函数
            scientific_functions = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 
                                  'log', 'ln', 'sqrt', 'factorial', 'abs', 'ceil', 'floor']
            
            for func in scientific_functions:
                pattern = f'{func}\\('
                if re.search(pattern, expression):
                    # 简单的函数替换（这里只处理单参数函数）
                    def replace_func(match):
                        func_name = match.group(0)[:-1]  # 去掉左括号
                        # 找到匹配的右括号
                        start = match.end() - 1
                        paren_count = 1
                        end = start + 1
                        while end < len(expression) and paren_count > 0:
                            if expression[end] == '(':
                                paren_count += 1
                            elif expression[end] == ')':
                                paren_count -= 1
                            end += 1
                        
                        if paren_count == 0:
                            arg = expression[start+1:end-1]
                            try:
                                arg_value = float(arg)
                                result = self.scientific_calculate(func_name, arg_value)
                                return str(result)
                            except:
                                return match.group(0)
                        return match.group(0)
                    
                    expression = re.sub(f'{func}\\([^)]*\\)', replace_func, expression)
            
            # 使用eval计算表达式（注意：在生产环境中应该使用更安全的表达式解析器）
            result = eval(expression)
            
            # 处理结果
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)  # 保留10位小数
            
            return result
            
        except Exception as e:
            raise ValueError(f"表达式计算错误：{e}")
    
    def calculate(self, expression):
        """
        计算表达式并记录历史
        """
        try:
            result = self.evaluate_expression(expression)
            self.add_to_history(expression, result)
            return result
        except Exception as e:
            raise ValueError(str(e))
    
    def show_history(self, limit=10):
        """
        显示历史记录
        """
        if not self.history:
            print("没有历史记录")
            return
        
        print(f"\n=== 最近{min(limit, len(self.history))}条计算记录 ===")
        print(f"{'时间':<20} {'表达式':<30} {'结果':<15}")
        print("-" * 70)
        
        for record in self.history[-limit:]:
            print(f"{record['timestamp']:<20} {record['expression']:<30} {record['result']:<15}")
    
    def clear_history(self):
        """
        清空历史记录
        """
        self.history = []
        self.save_history()
        print("历史记录已清空")
    
    def interactive_mode(self):
        """
        交互模式
        """
        print("=== 计算器程序 ===")
        print("输入表达式进行计算，输入'help'查看帮助，输入'quit'退出")
        print("支持基本运算：+ - * / ** %")
        print("支持科学函数：sin, cos, tan, asin, acos, atan, log, ln, sqrt, factorial, abs, ceil, floor")
        print("支持常数：π (pi), e")
        print("示例：2+3*4, sin(30), sqrt(16), log(100)")
        
        while True:
            try:
                user_input = input("\n请输入表达式: ").strip()
                
                if user_input.lower() == 'quit':
                    print("感谢使用计算器！")
                    break
                elif user_input.lower() == 'help':
                    self.show_help()
                elif user_input.lower() == 'history':
                    self.show_history()
                elif user_input.lower() == 'clear':
                    self.clear_history()
                elif user_input == '':
                    continue
                else:
                    result = self.calculate(user_input)
                    print(f"结果: {result}")
            
            except ValueError as e:
                print(f"错误: {e}")
            except KeyboardInterrupt:
                print("\n\n程序被中断，感谢使用！")
                break
            except Exception as e:
                print(f"未知错误: {e}")
    
    def show_help(self):
        """
        显示帮助信息
        """
        print("\n=== 计算器帮助 ===")
        print("基本运算:")
        print("  + 加法    - 减法    * 乘法    / 除法")
        print("  ** 幂运算  % 取模")
        print("\n科学函数:")
        print("  sin(x)    cos(x)    tan(x)    三角函数（角度制）")
        print("  asin(x)   acos(x)   atan(x)   反三角函数（返回角度）")
        print("  log(x)    常用对数   ln(x)     自然对数")
        print("  sqrt(x)   平方根    factorial(x) 阶乘")
        print("  abs(x)    绝对值    ceil(x)   向上取整   floor(x) 向下取整")
        print("\n常数:")
        print("  π (pi)    圆周率    e         自然常数")
        print("\n命令:")
        print("  help      显示帮助   history   显示历史")
        print("  clear     清空历史   quit      退出程序")
        print("\n示例:")
        print("  2+3*4     = 14")
        print("  sin(30)   = 0.5")
        print("  sqrt(16)  = 4")
        print("  log(100)  = 2")
        print("  2**3      = 8")

def main():
    """
    主函数
    """
    calculator = Calculator()
    
    # 演示一些计算
    print("=== 计算器演示 ===")
    
    test_expressions = [
        "2+3*4",
        "sin(30)",
        "sqrt(16)",
        "log(100)",
        "2**3",
        "factorial(5)",
        "abs(-5)",
        "ceil(3.2)",
        "floor(3.8)"
    ]
    
    for expr in test_expressions:
        try:
            result = calculator.calculate(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"{expr} = 错误: {e}")
    
    # 显示历史记录
    calculator.show_history()
    
    # 启动交互模式
    print("\n" + "="*50)
    calculator.interactive_mode()

if __name__ == "__main__":
    main()
