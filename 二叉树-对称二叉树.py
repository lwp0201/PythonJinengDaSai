# 二叉树-对称二叉树
# 题目: 给定一个二叉树的根节点，检查它是否是轴对称的。
# 轴对称定义：如果一个树的左子树与右子树镜像对称，那么这个树是对称的。

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归法
def isSymmetric(root):
    """
    递归法判断二叉树是否对称
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否对称
    """
    if not root:
        return True
    
    def isMirror(left, right):
        # 如果两个节点都为空，则对称
        if not left and not right:
            return True
        
        # 如果只有一个节点为空，则不对称
        if not left or not right:
            return False
        
        # 检查当前节点值是否相等，以及左右子树是否镜像对称
        return (left.val == right.val and 
                isMirror(left.left, right.right) and 
                isMirror(left.right, right.left))
    
    return isMirror(root.left, root.right)

# 方法二：迭代法（使用队列）
def isSymmetricIterative(root):
    """
    迭代法判断二叉树是否对称
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否对称
    """
    if not root:
        return True
    
    from collections import deque
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        
        # 如果两个节点都为空，继续检查下一对
        if not left and not right:
            continue
        
        # 如果只有一个节点为空，则不对称
        if not left or not right:
            return False
        
        # 如果节点值不相等，则不对称
        if left.val != right.val:
            return False
        
        # 将需要比较的节点对加入队列
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    
    return True

# 方法三：迭代法（使用栈）
def isSymmetricStack(root):
    """
    使用栈的迭代法判断二叉树是否对称
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否对称
    """
    if not root:
        return True
    
    stack = [(root.left, root.right)]
    
    while stack:
        left, right = stack.pop()
        
        # 如果两个节点都为空，继续检查下一对
        if not left and not right:
            continue
        
        # 如果只有一个节点为空，则不对称
        if not left or not right:
            return False
        
        # 如果节点值不相等，则不对称
        if left.val != right.val:
            return False
        
        # 将需要比较的节点对加入栈
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    
    return True

# 测试代码
if __name__ == "__main__":
    # 测试用例1：对称二叉树
    #      1
    #     / \
    #    2   2
    #   / \ / \
    #  3  4 4  3
    node3_left = TreeNode(3)
    node4_left = TreeNode(4)
    node2_left = TreeNode(2, node3_left, node4_left)
    
    node3_right = TreeNode(3)
    node4_right = TreeNode(4)
    node2_right = TreeNode(2, node4_right, node3_right)
    
    root1 = TreeNode(1, node2_left, node2_right)
    
    print("测试用例1（对称二叉树）：")
    print("递归法结果：", isSymmetric(root1))
    print("队列迭代法结果：", isSymmetricIterative(root1))
    print("栈迭代法结果：", isSymmetricStack(root1))
    
    # 测试用例2：不对称二叉树
    #      1
    #     / \
    #    2   2
    #     \   \
    #      3   3
    node3_left = TreeNode(3)
    node2_left = TreeNode(2, None, node3_left)
    
    node3_right = TreeNode(3)
    node2_right = TreeNode(2, None, node3_right)
    
    root2 = TreeNode(1, node2_left, node2_right)
    
    print("\n测试用例2（不对称二叉树）：")
    print("递归法结果：", isSymmetric(root2))
    print("队列迭代法结果：", isSymmetricIterative(root2))
    print("栈迭代法结果：", isSymmetricStack(root2))
