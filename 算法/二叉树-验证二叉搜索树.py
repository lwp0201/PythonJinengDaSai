# 二叉树-验证二叉搜索树
# 题目: 给定一个二叉树的根节点，判断其是否是一个有效的二叉搜索树。
# 二叉搜索树定义：
# 1. 节点的左子树只包含小于当前节点的数
# 2. 节点的右子树只包含大于当前节点的数
# 3. 所有左子树和右子树自身必须也是二叉搜索树

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归法（使用上下界）
def isValidBST(root):
    """
    递归法验证二叉搜索树
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否为有效的二叉搜索树
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        # 检查当前节点值是否在有效范围内
        if node.val <= min_val or node.val >= max_val:
            return False
        
        # 递归检查左右子树
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# 方法二：中序遍历法
def isValidBSTInorder(root):
    """
    中序遍历法验证二叉搜索树
    二叉搜索树的中序遍历结果应该是严格递增的
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否为有效的二叉搜索树
    """
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    
    # 检查是否严格递增
    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False
    
    return True

# 方法三：迭代中序遍历法
def isValidBSTIterative(root):
    """
    迭代中序遍历法验证二叉搜索树
    :param root: TreeNode，二叉树的根节点
    :return: bool，是否为有效的二叉搜索树
    """
    if not root:
        return True
    
    stack = []
    prev = None
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        
        if prev and root.val <= prev.val:
            return False
        
        prev = root
        root = root.right
    
    return True

# 测试代码
if __name__ == "__main__":
    # 测试用例1：有效的二叉搜索树
    #      5
    #     / \
    #    3   7
    #   / \
    #  2   4
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node2, node4)
    node7 = TreeNode(7)
    root1 = TreeNode(5, node3, node7)
    
    print("测试用例1（有效BST）：")
    print("递归法结果：", isValidBST(root1))
    print("中序遍历法结果：", isValidBSTInorder(root1))
    print("迭代中序遍历法结果：", isValidBSTIterative(root1))
    
    # 测试用例2：无效的二叉搜索树
    #      5
    #     / \
    #    3   7
    #   / \
    #  2   6  (6 > 5，违反了BST性质)
    node2 = TreeNode(2)
    node6 = TreeNode(6)
    node3 = TreeNode(3, node2, node6)
    node7 = TreeNode(7)
    root2 = TreeNode(5, node3, node7)
    
    print("\n测试用例2（无效BST）：")
    print("递归法结果：", isValidBST(root2))
    print("中序遍历法结果：", isValidBSTInorder(root2))
    print("迭代中序遍历法结果：", isValidBSTIterative(root2))
