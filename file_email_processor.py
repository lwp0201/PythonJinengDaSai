import os
import re


def process_emails_from_file(dir_name, file_path):
    """
    文件与邮箱处理函数
    
    参数:
        dir_name (str): 目录名称
        file_path (str): 文件路径
    
    返回:
        bool: 成功返回True，失败返回False
    """
    try:
        # 1. 创建目录
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        # 2. 读取文件
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 3. 提取邮箱 - 使用正则表达式
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, content)
        
        # 4. 去重处理
        unique_emails = list(set(emails))
        
        # 5. 在dir_name目录下创建data.txt文件
        data_file_path = os.path.join(dir_name, 'data.txt')
        with open(data_file_path, 'w', encoding='utf-8') as data_file:
            # 6. 将去重后的邮箱写入文件，一行一个
            for email in unique_emails:
                data_file.write(email + '\n')
        
        # 7. 关闭文件（with语句自动处理）
        return True
        
    except Exception as e:
        # 8. 捕获错误并返回False
        print(f"处理过程中出现错误: {e}")
        return False


def main():
    """主函数测试用例"""
    print("=== 文件与邮箱处理测试 ===")
    
    # 测试用例1：正常情况
    print("\n测试用例1：正常处理")
    test_file_path = "test_emails.txt"
    
    # 创建测试文件
    test_content = """
    联系邮箱：zhang@example.com
    技术支持：support@company.com
    客服邮箱：service@company.com
    重复邮箱：zhang@example.com
    另一个邮箱：admin@test.org
    无效邮箱：not-an-email
    有效邮箱：user123@gmail.com
    """
    
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    result1 = process_emails_from_file("output_dir", test_file_path)
    print(f"处理结果: {result1}")
    
    # 检查输出文件
    if os.path.exists("output_dir/data.txt"):
        with open("output_dir/data.txt", 'r', encoding='utf-8') as f:
            emails = f.read().strip().split('\n')
        print(f"提取到的邮箱: {emails}")
    
    # 测试用例2：文件不存在
    print("\n测试用例2：文件不存在")
    result2 = process_emails_from_file("output_dir2", "nonexistent.txt")
    print(f"处理结果: {result2}")
    
    # 测试用例3：空文件
    print("\n测试用例3：空文件")
    empty_file = "empty.txt"
    with open(empty_file, 'w', encoding='utf-8') as f:
        f.write("")
    
    result3 = process_emails_from_file("output_dir3", empty_file)
    print(f"处理结果: {result3}")
    
    # 清理测试文件
    try:
        os.remove(test_file_path)
        os.remove(empty_file)
        print("\n测试文件已清理")
    except:
        pass


if __name__ == "__main__":
    main()
