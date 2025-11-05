# 二叉树-二叉树的层序遍历
# 题目: 给定一个二叉树，返回其按层序遍历得到的节点值。
# 层序遍历：逐层地，从左到右访问所有节点。

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：使用队列的迭代法
def levelOrder(root):
    """
    使用队列实现二叉树的层序遍历
    :param root: TreeNode，二叉树的根节点
    :return: list，层序遍历结果
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # 处理当前层的所有节点
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # 将子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# 方法二：递归法
def levelOrderRecursive(root):
    """
    递归法实现二叉树的层序遍历
    :param root: TreeNode，二叉树的根节点
    :return: list，层序遍历结果
    """
    if not root:
        return []
    
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # 如果当前层还没有在结果中，添加新层
        if level >= len(result):
            result.append([])
        
        # 将当前节点值添加到对应层
        result[level].append(node.val)
        
        # 递归处理左右子树
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result

# 方法三：返回每层最右边的节点（右视图）
def rightSideView(root):
    """
    返回二叉树的右视图（每层最右边的节点）
    :param root: TreeNode，二叉树的根节点
    :return: list，右视图结果
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        # 处理当前层的所有节点
        for i in range(level_size):
            node = queue.popleft()
            
            # 如果是当前层的最后一个节点，加入结果
            if i == level_size - 1:
                result.append(node.val)
            
            # 将子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# 方法四：返回每层最左边的节点（左视图）
def leftSideView(root):
    """
    返回二叉树的左视图（每层最左边的节点）
    :param root: TreeNode，二叉树的根节点
    :return: list，左视图结果
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        # 处理当前层的所有节点
        for i in range(level_size):
            node = queue.popleft()
            
            # 如果是当前层的第一个节点，加入结果
            if i == 0:
                result.append(node.val)
            
            # 将子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# 测试代码
if __name__ == "__main__":
    # 构造如下二叉树
    #      3
    #     / \
    #    9   20
    #       / \
    #      15  7
    node9 = TreeNode(9)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)
    root = TreeNode(3, node9, node20)
    
    print("层序遍历结果（队列法）：", levelOrder(root))
    print("层序遍历结果（递归法）：", levelOrderRecursive(root))
    print("右视图结果：", rightSideView(root))
    print("左视图结果：", leftSideView(root))
    
    # 测试更复杂的二叉树
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, None, node6)
    root2 = TreeNode(1, node2, node3)
    
    print("\n更复杂的二叉树：")
    print("层序遍历结果：", levelOrder(root2))
    print("右视图结果：", rightSideView(root2))
    print("左视图结果：", leftSideView(root2))

