# 二叉树-二叉树的最大深度
# 题目: 给定一个二叉树，找出其最大深度。最大深度是从根节点到最远叶子节点的最长路径上的节点数。
# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 计算二叉树的最大深度
def maxDepth(root):
    """
    递归法，返回二叉树的最大深度
    :param root: TreeNode，二叉树的根节点
    :return: int，最大深度
    """
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

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

    print("二叉树的最大深度为：", maxDepth(root))
