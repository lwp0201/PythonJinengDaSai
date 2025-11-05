class BookError(Exception):
    """Book类自定义异常"""
    pass


class Book:
    """Book类 - 书籍信息管理"""
    
    # 类属性，用于排序
    sort_by = 'book_id'  # 默认按book_id排序
    
    def __init__(self, book_id, name, author=None, price=None, year=None):
        """
        初始化Book类的所有属性
        
        参数:
            book_id (str): 书籍ID，需为13位纯数字字符串
            name (str): 书名，字符串类型，不为空
            author (str): 作者，可为空
            price (float): 价格，需大于0
            year (int): 出版年份，可为空
        """
        # 验证book_id
        if not isinstance(book_id, str) or not book_id or len(book_id) != 13 or not book_id.isdigit():
            raise BookError("book_id必须为13位纯数字字符串且不为空")
        self.book_id = book_id
        
        # 验证name
        if not isinstance(name, str) or not name.strip():
            raise BookError("name必须为字符串类型且不为空")
        self.name = name.strip()
        
        # 验证author（可为空）
        if author is not None and not isinstance(author, str):
            raise BookError("author必须为字符串类型")
        self.author = author
        
        # 验证price
        if price is None or not isinstance(price, (int, float)) or price <= 0:
            raise BookError("price必须大于0且不为空")
        self.price = float(price)
        
        # 验证year（可为空）
        if year is not None and not isinstance(year, int):
            raise BookError("year必须为整数类型")
        self.year = year
    
    def get_info(self):
        """
        返回书籍的详细信息
        
        返回:
            str: 格式化的书籍信息
        """
        info_parts = [f"《{self.name}》"]
        
        if self.author:
            info_parts.append(f"-{self.author}")
        
        if self.year:
            info_parts.append(f"-{self.year}")
        
        info_parts.append(f"-{self.price} 元")
        
        return "".join(info_parts)
    
    def discount(self, rate):
        """
        根据折扣率计算折扣后的价格
        
        参数:
            rate (float): 折扣率，0 < rate <= 1
        
        返回:
            float: 折扣后的价格
        """
        if not isinstance(rate, (int, float)) or rate <= 0 or rate > 1:
            return self.price
        
        return round(self.price * rate, 2)
    
    def to_dict(self):
        """
        将Book类对象转换为字典
        
        返回:
            dict: 包含书籍信息的字典，空值不添加对应的键
        """
        result = {
            'book_id': self.book_id,
            'name': self.name,
            'price': self.price
        }
        
        if self.author is not None:
            result['author'] = self.author
        
        if self.year is not None:
            result['year'] = self.year
        
        return result
    
    def __lt__(self, other):
        """
        小于比较方法，支持排序
        
        参数:
            other (Book): 另一个Book对象
        
        返回:
            bool: 比较结果
        """
        if not isinstance(other, Book):
            return NotImplemented
        
        if Book.sort_by == 'book_id':
            return self.book_id < other.book_id
        elif Book.sort_by == 'price':
            return self.price < other.price
        else:
            return self.book_id < other.book_id
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.book_id == other.book_id
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return self.get_info()
    
    def __repr__(self):
        return f"Book(book_id='{self.book_id}', name='{self.name}', author='{self.author}', price={self.price}, year={self.year})"


def main():
    """主函数测试用例"""
    print("=== Book类测试 ===")
    
    # 测试用例1：正常创建Book对象
    print("\n测试用例1：正常创建Book对象")
    try:
        book1 = Book("1234567890123", "Python编程", "张三", 59.9, 2020)
        print(f"创建成功: {book1}")
        print(f"详细信息: {book1.get_info()}")
        print(f"字典格式: {book1.to_dict()}")
        print(f"8折价格: {book1.discount(0.8)}")
    except BookError as e:
        print(f"创建失败: {e}")
    
    # 测试用例2：缺少作者和年份
    print("\n测试用例2：缺少作者和年份")
    try:
        book2 = Book("1234567890124", "算法导论", None, 89.9, None)
        print(f"创建成功: {book2}")
        print(f"详细信息: {book2.get_info()}")
        print(f"字典格式: {book2.to_dict()}")
    except BookError as e:
        print(f"创建失败: {e}")
    
    # 测试用例3：无效参数
    print("\n测试用例3：无效参数测试")
    test_cases = [
        ("123456789012", "书名", None, 50.0, 2020),  # book_id长度不对
        ("", "书名", None, 50.0, 2020),  # book_id为空
        ("1234567890123", "", None, 50.0, 2020),  # name为空
        ("1234567890123", "书名", None, -10.0, 2020),  # price为负数
        ("1234567890123", "书名", None, None, 2020),  # price为None
    ]
    
    for i, (book_id, name, author, price, year) in enumerate(test_cases, 1):
        try:
            book = Book(book_id, name, author, price, year)
            print(f"测试{i}：意外成功 - {book}")
        except BookError as e:
            print(f"测试{i}：正确捕获错误 - {e}")
    
    # 测试用例4：排序功能
    print("\n测试用例4：排序功能测试")
    try:
        books = [
            Book("1234567890123", "Python编程", "张三", 59.9, 2020),
            Book("1234567890121", "Java编程", "李四", 69.9, 2019),
            Book("1234567890125", "C++编程", "王五", 79.9, 2021),
        ]
        
        # 按book_id排序
        Book.sort_by = 'book_id'
        books_sorted_by_id = sorted(books)
        print("按book_id排序:")
        for book in books_sorted_by_id:
            print(f"  {book.book_id} - {book.name}")
        
        # 按price排序
        Book.sort_by = 'price'
        books_sorted_by_price = sorted(books)
        print("按price排序:")
        for book in books_sorted_by_price:
            print(f"  {book.price} - {book.name}")
            
    except BookError as e:
        print(f"排序测试失败: {e}")
    
    # 测试用例5：折扣功能
    print("\n测试用例5：折扣功能测试")
    try:
        book = Book("1234567890123", "测试书籍", "测试作者", 100.0, 2023)
        print(f"原价: {book.price}")
        print(f"8折: {book.discount(0.8)}")
        print(f"5折: {book.discount(0.5)}")
        print(f"无效折扣(-0.1): {book.discount(-0.1)}")
        print(f"无效折扣(1.5): {book.discount(1.5)}")
    except BookError as e:
        print(f"折扣测试失败: {e}")


if __name__ == "__main__":
    main()
