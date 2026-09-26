class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map to look up node values in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            # Base case: no elements in the current subtree
            if in_left > in_right:
                return None

            # Pick current root from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Split point in inorder traversal
            mid = inorder_map[root_val]

            # Build left and right subtrees
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)