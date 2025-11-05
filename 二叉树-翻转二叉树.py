# 二叉树-翻转二叉树
# 题目: 给定一个二叉树的根节点，翻转这棵二叉树，并返回其根节点。
# 翻转定义：交换每个节点的左右子树。

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归法
def invertTree(root):
    """
    递归法翻转二叉树
    :param root: TreeNode，二叉树的根节点
    :return: TreeNode，翻转后的根节点
    """
    if not root:
        return None
    
    # 交换左右子树
    root.left, root.right = root.right, root.left
    
    # 递归翻转左右子树
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# 方法二：递归法（更简洁的写法）
def invertTreeConcise(root):
    """
    递归法翻转二叉树（简洁版）
    :param root: TreeNode，二叉树的根节点
    :return: TreeNode，翻转后的根节点
    """
    if not root:
        return None
    
    # 递归翻转左右子树，然后交换
    left = invertTreeConcise(root.left)
    right = invertTreeConcise(root.right)
    
    root.left = right
    root.right = left
    
    return root

# 方法三：迭代法（使用队列）
def invertTreeIterative(root):
    """
    迭代法翻转二叉树（使用队列）
    :param root: TreeNode，二叉树的根节点
    :return: TreeNode，翻转后的根节点
    """
    if not root:
        return None
    
    from collections import deque
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # 交换当前节点的左右子树
        node.left, node.right = node.right, node.left
        
        # 将子节点加入队列
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root

# 方法四：迭代法（使用栈）
def invertTreeStack(root):
    """
    迭代法翻转二叉树（使用栈）
    :param root: TreeNode，二叉树的根节点
    :return: TreeNode，翻转后的根节点
    """
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        # 交换当前节点的左右子树
        node.left, node.right = node.right, node.left
        
        # 将子节点加入栈
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root

# 辅助函数：打印二叉树（层序遍历）
def printTree(root):
    """
    打印二叉树（层序遍历格式）
    :param root: TreeNode，二叉树的根节点
    """
    if not root:
        print("空树")
        return
    
    from collections import deque
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                current_level.append(None)
        
        result.append(current_level)
    
    print("二叉树层序遍历结果：", result)

# 测试代码
if __name__ == "__main__":
    # 构造如下二叉树
    #      4
    #     / \
    #    2   7
    #   / \ / \
    #  1  3 6  9
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    
    root = TreeNode(4, node2, node7)
    
    print("原始二叉树：")
    printTree(root)
    
    # 测试不同的翻转方法
    print("\n使用递归法翻转：")
    root1 = invertTree(root)
    printTree(root1)
    
    # 重新构造树进行测试
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    root = TreeNode(4, node2, node7)
    
    print("\n使用简洁递归法翻转：")
    root2 = invertTreeConcise(root)
    printTree(root2)
    
    # 重新构造树进行测试
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    root = TreeNode(4, node2, node7)
    
    print("\n使用队列迭代法翻转：")
    root3 = invertTreeIterative(root)
    printTree(root3)
    
    # 重新构造树进行测试
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    root = TreeNode(4, node2, node7)
    
    print("\n使用栈迭代法翻转：")
    root4 = invertTreeStack(root)
    printTree(root4)
