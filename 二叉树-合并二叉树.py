# 二叉树-合并二叉树
# 题目: 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，
# 两个二叉树的一些节点便会重叠。你需要将他们合并为一个新的二叉树。
# 合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
# 否则不为 NULL 的节点将直接作为新二叉树的节点。

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归法
def mergeTrees(root1, root2):
    """
    递归法合并两个二叉树
    :param root1: TreeNode，第一个二叉树的根节点
    :param root2: TreeNode，第二个二叉树的根节点
    :return: TreeNode，合并后的二叉树根节点
    """
    # 如果其中一个节点为空，返回另一个节点
    if not root1:
        return root2
    if not root2:
        return root1
    
    # 创建新节点，值为两个节点值的和
    merged = TreeNode(root1.val + root2.val)
    
    # 递归合并左右子树
    merged.left = mergeTrees(root1.left, root2.left)
    merged.right = mergeTrees(root1.right, root2.right)
    
    return merged

# 方法二：递归法（原地修改）
def mergeTreesInPlace(root1, root2):
    """
    递归法合并两个二叉树（原地修改root1）
    :param root1: TreeNode，第一个二叉树的根节点
    :param root2: TreeNode，第二个二叉树的根节点
    :return: TreeNode，合并后的二叉树根节点
    """
    if not root1:
        return root2
    if not root2:
        return root1
    
    # 将root2的值加到root1上
    root1.val += root2.val
    
    # 递归合并左右子树
    root1.left = mergeTreesInPlace(root1.left, root2.left)
    root1.right = mergeTreesInPlace(root1.right, root2.right)
    
    return root1

# 方法三：迭代法（使用栈）
def mergeTreesIterative(root1, root2):
    """
    迭代法合并两个二叉树（使用栈）
    :param root1: TreeNode，第一个二叉树的根节点
    :param root2: TreeNode，第二个二叉树的根节点
    :return: TreeNode，合并后的二叉树根节点
    """
    if not root1:
        return root2
    if not root2:
        return root1
    
    stack = [(root1, root2)]
    
    while stack:
        node1, node2 = stack.pop()
        
        # 将node2的值加到node1上
        node1.val += node2.val
        
        # 处理左子树
        if node1.left and node2.left:
            stack.append((node1.left, node2.left))
        elif not node1.left and node2.left:
            node1.left = node2.left
        
        # 处理右子树
        if node1.right and node2.right:
            stack.append((node1.right, node2.right))
        elif not node1.right and node2.right:
            node1.right = node2.right
    
    return root1

# 辅助函数：创建二叉树的副本
def copyTree(root):
    """
    创建二叉树的副本
    :param root: TreeNode，原二叉树的根节点
    :return: TreeNode，新二叉树的根节点
    """
    if not root:
        return None
    
    new_root = TreeNode(root.val)
    new_root.left = copyTree(root.left)
    new_root.right = copyTree(root.right)
    
    return new_root

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
    # 构造第一个二叉树
    #      1
    #     / \
    #    3   2
    #   /
    #  5
    node5 = TreeNode(5)
    node3 = TreeNode(3, node5, None)
    node2 = TreeNode(2)
    root1 = TreeNode(1, node3, node2)
    
    # 构造第二个二叉树
    #      2
    #     / \
    #    1   3
    #     \   \
    #      4   7
    node4 = TreeNode(4)
    node1 = TreeNode(1, None, node4)
    node7 = TreeNode(7)
    node3_2 = TreeNode(3, None, node7)
    root2 = TreeNode(2, node1, node3_2)
    
    print("第一个二叉树：")
    printTree(root1)
    
    print("\n第二个二叉树：")
    printTree(root2)
    
    # 测试递归法合并
    print("\n使用递归法合并：")
    merged1 = mergeTrees(copyTree(root1), copyTree(root2))
    printTree(merged1)
    
    # 测试原地修改法合并
    print("\n使用原地修改法合并：")
    root1_copy = copyTree(root1)
    root2_copy = copyTree(root2)
    merged2 = mergeTreesInPlace(root1_copy, root2_copy)
    printTree(merged2)
    
    # 测试迭代法合并
    print("\n使用迭代法合并：")
    root1_copy = copyTree(root1)
    root2_copy = copyTree(root2)
    merged3 = mergeTreesIterative(root1_copy, root2_copy)
    printTree(merged3)
    
    # 测试边界情况
    print("\n测试边界情况：")
    print("空树与有值树合并：")
    empty_tree = None
    merged4 = mergeTrees(empty_tree, copyTree(root1))
    printTree(merged4)
    
    print("\n有值树与空树合并：")
    merged5 = mergeTrees(copyTree(root1), empty_tree)
    printTree(merged5)

