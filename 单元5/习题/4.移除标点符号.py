import string


def remove_punctuation(s):
    """
    移除字符串中的所有标点符号（不使用maketrans）
    """
    result = ""
    for char in s:
        if char not in string.punctuation:
            result += char
    return result


# 示例使用
test_string = "Hello, world! This is a test string."
print(remove_punctuation(test_string))  # 输出: Hello world This is a test string