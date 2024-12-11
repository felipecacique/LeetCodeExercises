# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # time O(n) space O(n)
        # do a dfs, and once we find target we start keepping track of the distance. For the target children is simple, just pass dist-1 in the parameters. But for the parentes that we have alseady seen (the ones on the top of target, before we find target) we must return to them the children dist - 1 in the post order. However for the post order of the remainig trre nodes on the other branches, we must do dist + 1, so it does not change the dist value of that node.
        # also we must traverse the nodes from both direction, left to right and then right to left, so our logic can reach all nodes. 

        def dfs(node, dist, mode):
            
            if not node:
                return dist + 1

            if not target in topNodes: topNodes.add(node)
            
            if dist == 0:
                ans.add(node.val)

            if node == target:
                dist = k

            if mode == "left_to_right":
                left, right  = node.left, node.right
            else:
                left, right  = node.right, node.left

            dist = dfs(left, dist - 1, mode)
            dist = dfs(right, dist - 1, mode)
            
            if dist == 0: ans.add(node.val)

            if node in topNodes: return dist - 1

            return dist + 1

        ans = set()
        topNodes = set()
        dfs(root, -1, "left_to_right")
        topNodes = set()
        dfs(root, -1, "right_to_left")
        
        return list(ans)

