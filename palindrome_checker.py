def is_palindrome(text):
    """
    判断字符串是否为回文
    
    参数:
        text (str): 输入字符串
    
    返回:
        bool: 是否为回文
    """
    # 忽略大小写和空格
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]


def min_replacements_for_palindrome(text):
    """
    计算将字符串变为回文最少需要替换的字符数量
    
    参数:
        text (str): 输入字符串
    
    返回:
        int: 最少需要替换的字符数量
    """
    # 忽略大小写和空格
    cleaned = ''.join(text.lower().split())
    
    if not cleaned:  # 空字符串
        return 0
    
    # 使用双指针从两端向中间比较
    left, right = 0, len(cleaned) - 1
    replacements = 0
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            replacements += 1
        left += 1
        right -= 1
    
    return replacements


def main():
    """主函数测试用例"""
    print("=== 回文字符串测试 ===")
    
    # 基本测试
    test_cases = ["", "Level", "abcde", "racecar", "hello"]
    
    for text in test_cases:
        is_pal = is_palindrome(text)
        replacements = min_replacements_for_palindrome(text)
        print(f"'{text}' -> 回文: {is_pal}, 最少替换: {replacements}")


if __name__ == "__main__":
    main()
