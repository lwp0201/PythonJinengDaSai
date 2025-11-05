# 字符处理-字符串操作
'''
题目: 字符处理和字符串操作相关的算法
要求掌握字符处理的基本编程方法

例如：
1. 字符串反转
2. 判断字符串是否为回文
3. 统计字符出现次数
4. 字符串去重
5. 字符串排序
6. 字符替换
'''

def reverse_string(s):
    """
    反转字符串
    :param s: str，待反转的字符串
    :return: str，反转后的字符串
    """
    # 方法一：切片
    return s[::-1]

def reverse_string_loop(s):
    """
    使用循环反转字符串
    :param s: str，待反转的字符串
    :return: str，反转后的字符串
    """
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

def reverse_string_recursive(s):
    """
    递归反转字符串
    :param s: str，待反转的字符串
    :return: str，反转后的字符串
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]

def is_palindrome_string(s):
    """
    判断字符串是否为回文
    :param s: str，待判断的字符串
    :return: bool，是否为回文
    """
    # 忽略大小写和空格
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_palindrome_string_loop(s):
    """
    使用循环判断字符串是否为回文
    :param s: str，待判断的字符串
    :return: bool，是否为回文
    """
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def count_characters(s):
    """
    统计字符串中每个字符的出现次数
    :param s: str，待统计的字符串
    :return: dict，字符及其出现次数的字典
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def count_characters_counter(s):
    """
    使用Counter统计字符出现次数
    :param s: str，待统计的字符串
    :return: dict，字符及其出现次数的字典
    """
    from collections import Counter
    return dict(Counter(s))

def remove_duplicates(s):
    """
    去除字符串中的重复字符
    :param s: str，待处理的字符串
    :return: str，去重后的字符串
    """
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

def remove_duplicates_order(s):
    """
    去除重复字符但保持原有顺序
    :param s: str，待处理的字符串
    :return: str，去重后的字符串
    """
    from collections import OrderedDict
    return "".join(OrderedDict.fromkeys(s))

def sort_string(s):
    """
    对字符串进行排序
    :param s: str，待排序的字符串
    :return: str，排序后的字符串
    """
    return "".join(sorted(s))

def sort_string_case_insensitive(s):
    """
    忽略大小写对字符串进行排序
    :param s: str，待排序的字符串
    :return: str，排序后的字符串
    """
    return "".join(sorted(s, key=str.lower))

def replace_characters(s, old_char, new_char):
    """
    替换字符串中的字符
    :param s: str，原字符串
    :param old_char: str，要替换的字符
    :param new_char: str，新字符
    :return: str，替换后的字符串
    """
    return s.replace(old_char, new_char)

def replace_characters_loop(s, old_char, new_char):
    """
    使用循环替换字符
    :param s: str，原字符串
    :param old_char: str，要替换的字符
    :param new_char: str，新字符
    :return: str，替换后的字符串
    """
    result = ""
    for char in s:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result

def find_first_non_repeating_char(s):
    """
    找到第一个不重复的字符
    :param s: str，待查找的字符串
    :return: str，第一个不重复的字符，如果没有返回None
    """
    char_count = count_characters(s)
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

def find_first_non_repeating_char_optimized(s):
    """
    优化的方法找到第一个不重复的字符
    :param s: str，待查找的字符串
    :return: str，第一个不重复的字符，如果没有返回None
    """
    from collections import Counter
    char_count = Counter(s)
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

def is_anagram(s1, s2):
    """
    判断两个字符串是否为字母异位词
    :param s1: str，第一个字符串
    :param s2: str，第二个字符串
    :return: bool，是否为字母异位词
    """
    # 忽略大小写和空格
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    return sorted(s1) == sorted(s2)

def is_anagram_counter(s1, s2):
    """
    使用Counter判断字母异位词
    :param s1: str，第一个字符串
    :param s2: str，第二个字符串
    :return: bool，是否为字母异位词
    """
    from collections import Counter
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    return Counter(s1) == Counter(s2)

def longest_common_prefix(strings):
    """
    找到字符串数组的最长公共前缀
    :param strings: list，字符串列表
    :return: str，最长公共前缀
    """
    if not strings:
        return ""
    
    if len(strings) == 1:
        return strings[0]
    
    prefix = strings[0]
    
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

def word_count(s):
    """
    统计字符串中的单词数
    :param s: str，待统计的字符串
    :return: int，单词数
    """
    words = s.split()
    return len(words)

def word_frequency(s):
    """
    统计单词频率
    :param s: str，待统计的字符串
    :return: dict，单词及其频率的字典
    """
    words = s.lower().split()
    word_count = {}
    
    for word in words:
        # 去除标点符号
        word = word.strip(".,!?;:")
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# 测试代码
if __name__ == "__main__":
    # 测试字符串反转
    test_string = "Hello World"
    print(f"原字符串: {test_string}")
    print(f"切片反转: {reverse_string(test_string)}")
    print(f"循环反转: {reverse_string_loop(test_string)}")
    print(f"递归反转: {reverse_string_recursive(test_string)}")
    
    # 测试回文判断
    palindrome_tests = ["racecar", "hello", "A man a plan a canal Panama", "race a car"]
    print(f"\n回文判断测试:")
    for s in palindrome_tests:
        print(f"'{s}': {is_palindrome_string(s)} (循环法: {is_palindrome_string_loop(s)})")
    
    # 测试字符统计
    test_text = "hello world"
    print(f"\n字符统计测试:")
    print(f"字符串: '{test_text}'")
    char_count1 = count_characters(test_text)
    char_count2 = count_characters_counter(test_text)
    print(f"字典法: {char_count1}")
    print(f"Counter法: {char_count2}")
    
    # 测试去重
    duplicate_string = "programming"
    print(f"\n去重测试:")
    print(f"原字符串: '{duplicate_string}'")
    print(f"去重后: '{remove_duplicates(duplicate_string)}'")
    print(f"保持顺序去重: '{remove_duplicates_order(duplicate_string)}'")
    
    # 测试排序
    sort_string_test = "programming"
    print(f"\n排序测试:")
    print(f"原字符串: '{sort_string_test}'")
    print(f"排序后: '{sort_string(sort_string_test)}'")
    print(f"忽略大小写排序: '{sort_string_case_insensitive('Hello World')}'")
    
    # 测试字符替换
    replace_test = "hello world"
    print(f"\n字符替换测试:")
    print(f"原字符串: '{replace_test}'")
    print(f"替换'l'为'L': '{replace_characters(replace_test, 'l', 'L')}'")
    print(f"循环替换: '{replace_characters_loop(replace_test, 'l', 'L')}'")
    
    # 测试第一个不重复字符
    non_repeat_test = "programming"
    print(f"\n第一个不重复字符测试:")
    print(f"字符串: '{non_repeat_test}'")
    print(f"第一个不重复字符: '{find_first_non_repeating_char(non_repeat_test)}'")
    print(f"优化方法: '{find_first_non_repeating_char_optimized(non_repeat_test)}'")
    
    # 测试字母异位词
    anagram_tests = [("listen", "silent"), ("hello", "world"), ("anagram", "nagaram")]
    print(f"\n字母异位词测试:")
    for s1, s2 in anagram_tests:
        print(f"'{s1}' 和 '{s2}': {is_anagram(s1, s2)} (Counter法: {is_anagram_counter(s1, s2)})")
    
    # 测试最长公共前缀
    prefix_tests = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["programming", "program", "programmer"]
    ]
    print(f"\n最长公共前缀测试:")
    for strings in prefix_tests:
        print(f"{strings}: '{longest_common_prefix(strings)}'")
    
    # 测试单词统计
    text = "Hello world! This is a test. Hello again."
    print(f"\n单词统计测试:")
    print(f"文本: '{text}'")
    print(f"单词数: {word_count(text)}")
    print(f"单词频率: {word_frequency(text)}")
    
    # 综合测试
    print(f"\n综合测试 - 字符串 '{test_string}':")
    print(f"反转: {reverse_string(test_string)}")
    print(f"是否为回文: {is_palindrome_string(test_string)}")
    print(f"字符统计: {count_characters(test_string)}")
    print(f"去重: {remove_duplicates(test_string)}")
    print(f"排序: {sort_string(test_string)}")
    print(f"第一个不重复字符: '{find_first_non_repeating_char(test_string)}'")

