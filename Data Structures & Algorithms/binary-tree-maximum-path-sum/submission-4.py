class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize max_sum to negative infinity to handle trees with negative values
        max_sum = float('-inf')
        
        def get_max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # If a child's path sum is negative, ignore it by taking max(..., 0)
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of the path if 'node' is the highest point (the peak/bend)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update our global maximum if this path beats our previous record
            max_sum = max(max_sum, current_path_sum)
            
            # Return the max gain this node can add to its parent (can only pick one branch)
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return max_sum