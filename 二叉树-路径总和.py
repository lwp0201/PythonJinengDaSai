# 二叉树-路径总和
# 题目: 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
# 这条路径上所有节点值相加等于目标和。

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一：递归法
def hasPathSum(root, targetSum):
    """
    递归法判断是否存在路径总和等于目标值
    :param root: TreeNode，二叉树的根节点
    :param targetSum: int，目标和
    :return: bool，是否存在这样的路径
    """
    if not root:
        return False
    
    # 如果是叶子节点，检查当前值是否等于剩余目标值
    if not root.left and not root.right:
        return root.val == targetSum
    
    # 递归检查左右子树
    remaining_sum = targetSum - root.val
    return (hasPathSum(root.left, remaining_sum) or 
            hasPathSum(root.right, remaining_sum))

# 方法二：迭代法（使用栈）
def hasPathSumIterative(root, targetSum):
    """
    迭代法判断是否存在路径总和等于目标值
    :param root: TreeNode，二叉树的根节点
    :param targetSum: int，目标和
    :return: bool，是否存在这样的路径
    """
    if not root:
        return False
    
    stack = [(root, targetSum - root.val)]
    
    while stack:
        node, remaining_sum = stack.pop()
        
        # 如果是叶子节点，检查是否达到目标
        if not node.left and not node.right:
            if remaining_sum == 0:
                return True
        
        # 将子节点和剩余目标值加入栈
        if node.left:
            stack.append((node.left, remaining_sum - node.left.val))
        if node.right:
            stack.append((node.right, remaining_sum - node.right.val))
    
    return False

# 扩展：返回所有路径总和等于目标值的路径
def pathSum(root, targetSum):
    """
    返回所有路径总和等于目标值的路径
    :param root: TreeNode，二叉树的根节点
    :param targetSum: int，目标和
    :return: list，所有符合条件的路径
    """
    if not root:
        return []
    
    result = []
    
    def dfs(node, current_path, remaining_sum):
        if not node:
            return
        
        current_path.append(node.val)
        
        # 如果是叶子节点且剩余和为0，找到一条路径
        if not node.left and not node.right and remaining_sum == node.val:
            result.append(current_path[:])
        else:
            # 递归搜索左右子树
            dfs(node.left, current_path, remaining_sum - node.val)
            dfs(node.right, current_path, remaining_sum - node.val)
        
        # 回溯
        current_path.pop()
    
    dfs(root, [], targetSum)
    return result

# 测试代码
if __name__ == "__main__":
    # 构造如下二叉树
    #      5
    #     / \
    #    4   8
    #   /   / \
    #  11  13  4
    # / \      \
    #7  2      1
    node7 = TreeNode(7)
    node2 = TreeNode(2)
    node11 = TreeNode(11, node7, node2)
    node4_left = TreeNode(4, node11, None)
    
    node13 = TreeNode(13)
    node1 = TreeNode(1)
    node4_right = TreeNode(4, None, node1)
    node8 = TreeNode(8, node13, node4_right)
    
    root = TreeNode(5, node4_left, node8)
    
    target = 22
    
    print(f"目标路径总和：{target}")
    print("递归法结果：", hasPathSum(root, target))
    print("迭代法结果：", hasPathSumIterative(root, target))
    print("所有路径：", pathSum(root, target))
    
    # 测试其他目标值
    print(f"\n目标路径总和：{26}")
    print("递归法结果：", hasPathSum(root, 26))
    print("所有路径：", pathSum(root, 26))
