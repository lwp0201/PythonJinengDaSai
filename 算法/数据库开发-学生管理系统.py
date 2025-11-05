# 数据库开发-学生管理系统
'''
题目: 开发一个学生管理系统，使用SQLite数据库
要求掌握数据库开发的基本方法

功能包括：
1. 创建学生表
2. 添加学生信息
3. 查询学生信息
4. 更新学生信息
5. 删除学生信息
6. 统计学生信息
'''

import sqlite3
import os
from datetime import datetime

class StudentManager:
    def __init__(self, db_name="students.db"):
        """
        初始化学生管理系统
        :param db_name: str，数据库文件名
        """
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """
        初始化数据库，创建学生表
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # 创建学生表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                major TEXT NOT NULL,
                grade REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print("数据库初始化完成！")
    
    def add_student(self, student_id, name, age, gender, major, grade=None):
        """
        添加学生信息
        :param student_id: str，学号
        :param name: str，姓名
        :param age: int，年龄
        :param gender: str，性别
        :param major: str，专业
        :param grade: float，成绩
        :return: bool，是否添加成功
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO students (student_id, name, age, gender, major, grade)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (student_id, name, age, gender, major, grade))
            
            conn.commit()
            conn.close()
            print(f"学生 {name} 添加成功！")
            return True
        except sqlite3.IntegrityError:
            print(f"学号 {student_id} 已存在！")
            return False
        except Exception as e:
            print(f"添加学生失败：{e}")
            return False
    
    def get_all_students(self):
        """
        获取所有学生信息
        :return: list，学生信息列表
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students ORDER BY student_id')
        students = cursor.fetchall()
        
        conn.close()
        return students
    
    def get_student_by_id(self, student_id):
        """
        根据学号查询学生信息
        :param student_id: str，学号
        :return: tuple，学生信息
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()
        
        conn.close()
        return student
    
    def get_students_by_major(self, major):
        """
        根据专业查询学生信息
        :param major: str，专业
        :return: list，学生信息列表
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students WHERE major = ? ORDER BY student_id', (major,))
        students = cursor.fetchall()
        
        conn.close()
        return students
    
    def update_student(self, student_id, **kwargs):
        """
        更新学生信息
        :param student_id: str，学号
        :param kwargs: dict，要更新的字段
        :return: bool，是否更新成功
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # 构建更新语句
            set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
            set_clause += ', updated_at = CURRENT_TIMESTAMP'
            
            values = list(kwargs.values()) + [student_id]
            
            cursor.execute(f'''
                UPDATE students 
                SET {set_clause}
                WHERE student_id = ?
            ''', values)
            
            if cursor.rowcount > 0:
                conn.commit()
                conn.close()
                print(f"学号 {student_id} 的信息更新成功！")
                return True
            else:
                conn.close()
                print(f"学号 {student_id} 不存在！")
                return False
        except Exception as e:
            print(f"更新学生信息失败：{e}")
            return False
    
    def delete_student(self, student_id):
        """
        删除学生信息
        :param student_id: str，学号
        :return: bool，是否删除成功
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            
            if cursor.rowcount > 0:
                conn.commit()
                conn.close()
                print(f"学号 {student_id} 的学生信息删除成功！")
                return True
            else:
                conn.close()
                print(f"学号 {student_id} 不存在！")
                return False
        except Exception as e:
            print(f"删除学生信息失败：{e}")
            return False
    
    def get_statistics(self):
        """
        获取学生统计信息
        :return: dict，统计信息
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # 总学生数
        cursor.execute('SELECT COUNT(*) FROM students')
        total_count = cursor.fetchone()[0]
        
        # 按性别统计
        cursor.execute('SELECT gender, COUNT(*) FROM students GROUP BY gender')
        gender_stats = dict(cursor.fetchall())
        
        # 按专业统计
        cursor.execute('SELECT major, COUNT(*) FROM students GROUP BY major')
        major_stats = dict(cursor.fetchall())
        
        # 平均成绩
        cursor.execute('SELECT AVG(grade) FROM students WHERE grade IS NOT NULL')
        avg_grade = cursor.fetchone()[0]
        
        # 最高成绩和最低成绩
        cursor.execute('SELECT MAX(grade), MIN(grade) FROM students WHERE grade IS NOT NULL')
        max_grade, min_grade = cursor.fetchone()
        
        conn.close()
        
        return {
            'total_count': total_count,
            'gender_stats': gender_stats,
            'major_stats': major_stats,
            'avg_grade': avg_grade,
            'max_grade': max_grade,
            'min_grade': min_grade
        }
    
    def search_students(self, keyword):
        """
        搜索学生信息
        :param keyword: str，搜索关键词
        :return: list，搜索结果
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM students 
            WHERE student_id LIKE ? OR name LIKE ? OR major LIKE ?
            ORDER BY student_id
        ''', (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
        
        students = cursor.fetchall()
        conn.close()
        return students
    
    def display_students(self, students):
        """
        显示学生信息
        :param students: list，学生信息列表
        """
        if not students:
            print("没有找到学生信息！")
            return
        
        print(f"{'学号':<12} {'姓名':<8} {'年龄':<4} {'性别':<4} {'专业':<12} {'成绩':<6}")
        print("-" * 60)
        
        for student in students:
            student_id, name, age, gender, major, grade = student[1:7]
            grade_str = f"{grade:.1f}" if grade is not None else "未录入"
            print(f"{student_id:<12} {name:<8} {age:<4} {gender:<4} {major:<12} {grade_str:<6}")
    
    def display_statistics(self):
        """
        显示统计信息
        """
        stats = self.get_statistics()
        
        print("\n=== 学生统计信息 ===")
        print(f"总学生数: {stats['total_count']}")
        
        print("\n按性别统计:")
        for gender, count in stats['gender_stats'].items():
            print(f"  {gender}: {count}人")
        
        print("\n按专业统计:")
        for major, count in stats['major_stats'].items():
            print(f"  {major}: {count}人")
        
        if stats['avg_grade'] is not None:
            print(f"\n成绩统计:")
            print(f"  平均成绩: {stats['avg_grade']:.2f}")
            print(f"  最高成绩: {stats['max_grade']:.2f}")
            print(f"  最低成绩: {stats['min_grade']:.2f}")
        else:
            print("\n暂无成绩数据")

def main():
    """
    主函数，演示学生管理系统的使用
    """
    # 创建学生管理系统实例
    sm = StudentManager()
    
    # 添加示例数据
    print("添加示例学生数据...")
    sm.add_student("2023001", "张三", 20, "男", "计算机科学", 85.5)
    sm.add_student("2023002", "李四", 19, "女", "软件工程", 92.0)
    sm.add_student("2023003", "王五", 21, "男", "计算机科学", 78.5)
    sm.add_student("2023004", "赵六", 20, "女", "数据科学", 88.0)
    sm.add_student("2023005", "钱七", 19, "男", "软件工程", 95.5)
    
    print("\n=== 所有学生信息 ===")
    all_students = sm.get_all_students()
    sm.display_students(all_students)
    
    print("\n=== 查询计算机科学专业的学生 ===")
    cs_students = sm.get_students_by_major("计算机科学")
    sm.display_students(cs_students)
    
    print("\n=== 查询学号为2023002的学生 ===")
    student = sm.get_student_by_id("2023002")
    if student:
        sm.display_students([student])
    
    print("\n=== 更新学生信息 ===")
    sm.update_student("2023001", grade=90.0, age=21)
    
    print("\n=== 搜索包含'张'的学生 ===")
    search_results = sm.search_students("张")
    sm.display_students(search_results)
    
    # 显示统计信息
    sm.display_statistics()
    
    print("\n=== 删除学生信息 ===")
    sm.delete_student("2023005")
    
    print("\n=== 删除后的所有学生信息 ===")
    remaining_students = sm.get_all_students()
    sm.display_students(remaining_students)

if __name__ == "__main__":
    main()

