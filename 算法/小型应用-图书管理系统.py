# 小型应用-图书管理系统
'''
题目: 开发一个图书管理系统
要求掌握小型应用项目程序的开发方法

功能包括：
1. 图书信息管理（增删改查）
2. 借阅管理
3. 用户管理
4. 统计报表
5. 数据持久化
'''

import json
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, publisher, year, copies=1):
        """
        图书类
        :param isbn: str，ISBN号
        :param title: str，书名
        :param author: str，作者
        :param publisher: str，出版社
        :param year: int，出版年份
        :param copies: int，副本数量
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.copies = copies
        self.available_copies = copies
        self.borrowed_copies = 0

class User:
    def __init__(self, user_id, name, email, user_type="student"):
        """
        用户类
        :param user_id: str，用户ID
        :param name: str，姓名
        :param email: str，邮箱
        :param user_type: str，用户类型（student/teacher/staff）
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.user_type = user_type
        self.borrowed_books = []
        self.borrow_history = []

class BorrowRecord:
    def __init__(self, user_id, isbn, borrow_date, return_date=None):
        """
        借阅记录类
        :param user_id: str，用户ID
        :param isbn: str，ISBN号
        :param borrow_date: str，借阅日期
        :param return_date: str，归还日期
        """
        self.user_id = user_id
        self.isbn = isbn
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.is_returned = return_date is not None

class LibrarySystem:
    def __init__(self):
        """
        初始化图书管理系统
        """
        self.books = {}  # ISBN -> Book
        self.users = {}  # user_id -> User
        self.borrow_records = []  # 借阅记录列表
        self.data_file = "library_data.json"
        self.load_data()
    
    def save_data(self):
        """
        保存数据到文件
        """
        data = {
            'books': {},
            'users': {},
            'borrow_records': []
        }
        
        # 保存图书数据
        for isbn, book in self.books.items():
            data['books'][isbn] = {
                'isbn': book.isbn,
                'title': book.title,
                'author': book.author,
                'publisher': book.publisher,
                'year': book.year,
                'copies': book.copies,
                'available_copies': book.available_copies,
                'borrowed_copies': book.borrowed_copies
            }
        
        # 保存用户数据
        for user_id, user in self.users.items():
            data['users'][user_id] = {
                'user_id': user.user_id,
                'name': user.name,
                'email': user.email,
                'user_type': user.user_type,
                'borrowed_books': user.borrowed_books,
                'borrow_history': user.borrow_history
            }
        
        # 保存借阅记录
        for record in self.borrow_records:
            data['borrow_records'].append({
                'user_id': record.user_id,
                'isbn': record.isbn,
                'borrow_date': record.borrow_date,
                'return_date': record.return_date,
                'is_returned': record.is_returned
            })
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        """
        从文件加载数据
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # 加载图书数据
                for isbn, book_data in data.get('books', {}).items():
                    book = Book(
                        book_data['isbn'],
                        book_data['title'],
                        book_data['author'],
                        book_data['publisher'],
                        book_data['year'],
                        book_data['copies']
                    )
                    book.available_copies = book_data['available_copies']
                    book.borrowed_copies = book_data['borrowed_copies']
                    self.books[isbn] = book
                
                # 加载用户数据
                for user_id, user_data in data.get('users', {}).items():
                    user = User(
                        user_data['user_id'],
                        user_data['name'],
                        user_data['email'],
                        user_data['user_type']
                    )
                    user.borrowed_books = user_data['borrowed_books']
                    user.borrow_history = user_data['borrow_history']
                    self.users[user_id] = user
                
                # 加载借阅记录
                for record_data in data.get('borrow_records', []):
                    record = BorrowRecord(
                        record_data['user_id'],
                        record_data['isbn'],
                        record_data['borrow_date'],
                        record_data['return_date']
                    )
                    record.is_returned = record_data['is_returned']
                    self.borrow_records.append(record)
                
                print("数据加载成功！")
            except Exception as e:
                print(f"数据加载失败：{e}")
        else:
            print("未找到数据文件，将创建新的数据库")
    
    def add_book(self, isbn, title, author, publisher, year, copies=1):
        """
        添加图书
        """
        if isbn in self.books:
            self.books[isbn].copies += copies
            self.books[isbn].available_copies += copies
            print(f"图书 {title} 的副本数量已更新")
        else:
            self.books[isbn] = Book(isbn, title, author, publisher, year, copies)
            print(f"图书 {title} 添加成功")
        
        self.save_data()
    
    def add_user(self, user_id, name, email, user_type="student"):
        """
        添加用户
        """
        if user_id in self.users:
            print(f"用户ID {user_id} 已存在")
            return False
        
        self.users[user_id] = User(user_id, name, email, user_type)
        print(f"用户 {name} 添加成功")
        self.save_data()
        return True
    
    def search_books(self, keyword):
        """
        搜索图书
        """
        results = []
        keyword = keyword.lower()
        
        for book in self.books.values():
            if (keyword in book.title.lower() or 
                keyword in book.author.lower() or 
                keyword in book.publisher.lower() or
                keyword in book.isbn):
                results.append(book)
        
        return results
    
    def borrow_book(self, user_id, isbn):
        """
        借阅图书
        """
        if user_id not in self.users:
            print("用户不存在")
            return False
        
        if isbn not in self.books:
            print("图书不存在")
            return False
        
        book = self.books[isbn]
        user = self.users[user_id]
        
        if book.available_copies <= 0:
            print("图书已全部借出")
            return False
        
        if len(user.borrowed_books) >= 5:  # 限制借阅数量
            print("借阅数量已达上限")
            return False
        
        # 检查是否已借阅
        if isbn in user.borrowed_books:
            print("您已借阅此书")
            return False
        
        # 执行借阅
        book.available_copies -= 1
        book.borrowed_copies += 1
        user.borrowed_books.append(isbn)
        
        # 记录借阅
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        record = BorrowRecord(user_id, isbn, borrow_date)
        self.borrow_records.append(record)
        user.borrow_history.append(borrow_date)
        
        print(f"借阅成功！借阅日期：{borrow_date}")
        self.save_data()
        return True
    
    def return_book(self, user_id, isbn):
        """
        归还图书
        """
        if user_id not in self.users:
            print("用户不存在")
            return False
        
        if isbn not in self.books:
            print("图书不存在")
            return False
        
        user = self.users[user_id]
        
        if isbn not in user.borrowed_books:
            print("您未借阅此书")
            return False
        
        # 执行归还
        book = self.books[isbn]
        book.available_copies += 1
        book.borrowed_copies -= 1
        user.borrowed_books.remove(isbn)
        
        # 更新借阅记录
        return_date = datetime.now().strftime("%Y-%m-%d")
        for record in self.borrow_records:
            if (record.user_id == user_id and 
                record.isbn == isbn and 
                not record.is_returned):
                record.return_date = return_date
                record.is_returned = True
                break
        
        print(f"归还成功！归还日期：{return_date}")
        self.save_data()
        return True
    
    def display_books(self, books=None):
        """
        显示图书信息
        """
        if books is None:
            books = list(self.books.values())
        
        if not books:
            print("没有找到图书")
            return
        
        print(f"{'ISBN':<15} {'书名':<20} {'作者':<15} {'出版社':<15} {'年份':<6} {'总副本':<6} {'可借':<6}")
        print("-" * 90)
        
        for book in books:
            print(f"{book.isbn:<15} {book.title:<20} {book.author:<15} "
                  f"{book.publisher:<15} {book.year:<6} {book.copies:<6} {book.available_copies:<6}")
    
    def display_users(self):
        """
        显示用户信息
        """
        if not self.users:
            print("没有用户")
            return
        
        print(f"{'用户ID':<10} {'姓名':<10} {'邮箱':<20} {'类型':<10} {'借阅数量':<8}")
        print("-" * 70)
        
        for user in self.users.values():
            print(f"{user.user_id:<10} {user.name:<10} {user.email:<20} "
                  f"{user.user_type:<10} {len(user.borrowed_books):<8}")
    
    def display_borrow_records(self, user_id=None):
        """
        显示借阅记录
        """
        records = self.borrow_records
        if user_id:
            records = [r for r in records if r.user_id == user_id]
        
        if not records:
            print("没有借阅记录")
            return
        
        print(f"{'用户ID':<10} {'ISBN':<15} {'借阅日期':<12} {'归还日期':<12} {'状态':<6}")
        print("-" * 60)
        
        for record in records:
            status = "已归还" if record.is_returned else "未归还"
            return_date = record.return_date if record.return_date else "未归还"
            print(f"{record.user_id:<10} {record.isbn:<15} {record.borrow_date:<12} "
                  f"{return_date:<12} {status:<6}")
    
    def get_statistics(self):
        """
        获取统计信息
        """
        total_books = len(self.books)
        total_users = len(self.users)
        total_borrows = len([r for r in self.borrow_records if not r.is_returned])
        
        # 按类型统计用户
        user_types = {}
        for user in self.users.values():
            user_types[user.user_type] = user_types.get(user.user_type, 0) + 1
        
        # 热门图书（借阅次数最多）
        borrow_counts = {}
        for record in self.borrow_records:
            borrow_counts[record.isbn] = borrow_counts.get(record.isbn, 0) + 1
        
        popular_books = sorted(borrow_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'total_books': total_books,
            'total_users': total_users,
            'total_borrows': total_borrows,
            'user_types': user_types,
            'popular_books': popular_books
        }
    
    def display_statistics(self):
        """
        显示统计信息
        """
        stats = self.get_statistics()
        
        print("\n=== 图书管理系统统计信息 ===")
        print(f"总图书数: {stats['total_books']}")
        print(f"总用户数: {stats['total_users']}")
        print(f"当前借阅数: {stats['total_borrows']}")
        
        print("\n用户类型分布:")
        for user_type, count in stats['user_types'].items():
            print(f"  {user_type}: {count}人")
        
        print("\n热门图书 (借阅次数前5):")
        for isbn, count in stats['popular_books']:
            book = self.books.get(isbn)
            if book:
                print(f"  {book.title} ({isbn}): {count}次")

def main():
    """
    主函数，演示图书管理系统的使用
    """
    # 创建图书管理系统实例
    library = LibrarySystem()
    
    # 添加示例图书
    print("添加示例图书...")
    library.add_book("978-0134685991", "Effective Python", "Brett Slatkin", "Addison-Wesley", 2019, 3)
    library.add_book("978-0132350884", "Clean Code", "Robert Martin", "Prentice Hall", 2008, 2)
    library.add_book("978-0134685991", "Effective Python", "Brett Slatkin", "Addison-Wesley", 2019, 1)  # 增加副本
    
    # 添加示例用户
    print("\n添加示例用户...")
    library.add_user("U001", "张三", "zhangsan@email.com", "student")
    library.add_user("U002", "李四", "lisi@email.com", "teacher")
    library.add_user("U003", "王五", "wangwu@email.com", "staff")
    
    # 显示图书信息
    print("\n=== 所有图书信息 ===")
    library.display_books()
    
    # 显示用户信息
    print("\n=== 所有用户信息 ===")
    library.display_users()
    
    # 搜索图书
    print("\n=== 搜索包含'Python'的图书 ===")
    python_books = library.search_books("Python")
    library.display_books(python_books)
    
    # 借阅图书
    print("\n=== 借阅图书 ===")
    library.borrow_book("U001", "978-0134685991")
    library.borrow_book("U002", "978-0134685991")
    library.borrow_book("U001", "978-0132350884")
    
    # 显示借阅记录
    print("\n=== 所有借阅记录 ===")
    library.display_borrow_records()
    
    # 归还图书
    print("\n=== 归还图书 ===")
    library.return_book("U001", "978-0134685991")
    
    # 显示归还后的借阅记录
    print("\n=== 归还后的借阅记录 ===")
    library.display_borrow_records()
    
    # 显示统计信息
    library.display_statistics()

if __name__ == "__main__":
    main()
