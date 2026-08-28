# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Do a preorder traversal of the tree
        # Store all the values in an array
        # Select the kth value afterward

        arr = []

        def preorderDFS(arr,node):

            if not node:
                return arr 

            preorderDFS(arr,node.left)
            arr.append(node.val)
            preorderDFS(arr,node.right)

        preorderDFS(arr,root)

        return arr[k-1]
        
        