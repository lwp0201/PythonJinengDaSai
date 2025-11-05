from abc import ABC, abstractmethod


class RectangleInterface(ABC):
    """矩形接口类"""
    
    @abstractmethod
    def perimeter(self):
        """计算并返回矩形的周长"""
        pass
    
    @abstractmethod
    def area(self):
        """计算并返回矩形的面积"""
        pass
    
    @abstractmethod
    def is_square(self):
        """判断矩形是否为正方形，返回布尔值"""
        pass


class Rectangle(RectangleInterface):
    """矩形类"""
    
    def __init__(self, length, width):
        """
        初始化矩形
        
        参数:
            length (float): 矩形的长
            width (float): 矩形的宽
        """
        if length <= 0 or width <= 0:
            raise ValueError("矩形的长和宽必须大于0")
        
        self.length = float(length)
        self.width = float(width)
    
    def perimeter(self):
        """
        计算并返回矩形的周长
        
        返回:
            float: 矩形的周长
        """
        return 2 * (self.length + self.width)
    
    def area(self):
        """
        计算并返回矩形的面积
        
        返回:
            float: 矩形的面积
        """
        return self.length * self.width
    
    def is_square(self):
        """
        判断矩形是否为正方形
        
        返回:
            bool: 是否为正方形
        """
        return abs(self.length - self.width) < 1e-9  # 考虑浮点数精度问题
    
    def __str__(self):
        """字符串表示"""
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def __repr__(self):
        """详细字符串表示"""
        return f"Rectangle({self.length}, {self.width})"


def main():
    """主函数测试用例"""
    print("=== 矩形类测试 ===")
    
    # 基本测试
    try:
        rect = Rectangle(5, 3)
        print(f"矩形: {rect}")
        print(f"周长: {rect.perimeter()}")
        print(f"面积: {rect.area()}")
        print(f"是否为正方形: {rect.is_square()}")
    except ValueError as e:
        print(f"创建失败: {e}")
    
    # 正方形测试
    try:
        square = Rectangle(4, 4)
        print(f"正方形: {square}")
        print(f"是否为正方形: {square.is_square()}")
    except ValueError as e:
        print(f"创建失败: {e}")
    
    # 异常情况测试
    try:
        invalid_rect = Rectangle(0, 5)
    except ValueError as e:
        print(f"正确捕获错误: {e}")


if __name__ == "__main__":
    main()