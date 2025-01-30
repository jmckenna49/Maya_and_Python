class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0  # Base case: If the tree is empty, depth is 0

        left_depth = self.maxDepth(root.left)   # Recursively find left subtree depth
        right_depth = self.maxDepth(root.right) # Recursively find right subtree depth

        return max(left_depth, right_depth) + 1  # Add 1 to account for the current node