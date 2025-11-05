def is_alphanumeric(s):
    """
    检查字符串是否仅包含字母和数字字符
    """
    for char in s:
        # 使用字符分类来判断是否是字母或数字
        if not (char.isalpha() or char.isdigit()):
            return False
    return True


# 示例使用
test_string1 = "hello123"
test_string2 = "hello_123"
print(is_alphanumeric(test_string1))  # 应输出 true
print(is_alphanumeric(test_string2))  # 应输出 false