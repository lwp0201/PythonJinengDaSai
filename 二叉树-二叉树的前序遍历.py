# 二叉树-二叉树的前序遍历
# 题目: 给定一个二叉树的根节点，返回它的前序遍历结果。
# 前序遍历：根节点 -> 左子树 -> 右子树

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归法实现前序遍历
def preorderTraversal(root):
    """
    递归法实现二叉树的前序遍历
    :param root: TreeNode，二叉树的根节点
    :return: list，前序遍历结果
    """
    result = []
    
    def preorder(node):
        if not node:
            return
        result.append(node.val)  # 访问根节点
        preorder(node.left)      # 遍历左子树
        preorder(node.right)     # 遍历右子树
    
    preorder(root)
    return result

# 迭代法实现前序遍历
def preorderTraversalIterative(root):
    """
    迭代法实现二叉树的前序遍历
    :param root: TreeNode，二叉树的根节点
    :return: list，前序遍历结果
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # 注意：先压入右子树，再压入左子树
        # 这样出栈时就是左子树先出栈
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# 测试代码
if __name__ == "__main__":
    # 构造如下二叉树
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    print("递归法前序遍历结果：", preorderTraversal(root))
    print("迭代法前序遍历结果：", preorderTraversalIterative(root))
