# 统计字符串中的字符类型
#题目: 编写一个函数，接收一个字符串，然后统计并返回该字符串中英文字母、数字、空格和其他字符的个数。
def count_char_types(s):
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0
    for ch in s:
        if ch.isalpha():
            letter_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch.isspace():
            space_count += 1
        else:
            other_count += 1
    return {
        "字母": letter_count,
        "数字": digit_count,
        "空格": space_count,
        "其他": other_count
    }

    # 测试代码
if __name__ == "__main__":
    test_str = input("请输入一个字符串：")
    result = count_char_types(test_str)
    print("统计结果：")
    for k, v in result.items():
        print(f"{k}个数: {v}")
