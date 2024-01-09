# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # we will do a DFS and store a list (harshtable) with all that node children. And then after we visit all its children, and we get to the parent node again, we check in the list if there is p and q. We do this in a post order travel, bottom to top, left to right. If we fallow this sequence, we will always process the parents node from the bottom to top, (with highest tree depth), thus we will get the LOWEST ancestor. Besides the children of the node(h) is the children of nodes[h+1] + nodes[h+1]. That way we only need no have one children list, and keep adding nodes to it and we move from bottom to top.

        def Solution1(root, p, q):
            lca = []

            def dfs(node):
                # stop criterium
                if node == None:
                    return set()

                # visit children
                children_left = dfs(node.left)
                children_right = dfs(node.right)

                children = set()  # a set of unique values
                children = children_left.union(children_right)  # merge the sets O(n)?

                # process the current node here (after we have visited the left and right - POST ORDER)
                children.add(node)  # O(1)

                # check if p and q is within its children. If so, we have found the LCA. And lets stop the tree search and return its node

                if (p.val in children) and (q.val in children):  # O(1)
                    lca.append(node.val)  # we have found the LCA

                return children

            dfs(root)

            return lca[0]

        def Solution2(root, p, q):
            # as w evisit the children we return a flag if p o q is in that branch. The node where left and right are both true, that is our LCA.

            lca = []

            def dfs(node):
                # stop criterium
                if node == None:
                    return False

                # visit children
                left = dfs(node.left)
                right = dfs(node.right)

                if (
                    (left == True and right == True)
                    or (left == True and node.val in [p.val, q.val])
                    or (right == True and node.val in [p.val, q.val])
                ):
                    lca.append(node)

                if node.val in [p.val, q.val] or left == True or right == True:
                    return True

                return False

            dfs(root)

            return lca[0]

        def Solution3(root, p, q):
            # as we visit the children we return a flag if p o q is in that branch. The node where left and right are both true, that is our LCA.

            def dfs(node):
                # stop criterium
                if not node:
                    return None

                # visit children
                left = dfs(node.left)
                right = dfs(node.right)

                is_p_or_q = node.val in [p.val, q.val]

                if (left == True and right == True) or (
                    (left == True or right == True) and is_p_or_q
                ):
                    return node

                return is_p_or_q or left or right

            node = dfs(root)

            return node

        def Solution4(root, p, q):
            # as we visit the children we return a flag if p o q is in that branch. The node where left and right are both true, that is our LCA. But lets do it itereatively, so we can just break the bfs and return the LCA. It will be a little quicker

            stack = [root]

            while stack != []:
                stack.append(node.right)
                stack.append(node.left)

                node = stack.pop()

                # visit children
                left = dfs(node.left)
                right = dfs(node.right)

                is_p_or_q = node.val in [p.val, q.val]

                if (left == True and right == True) or (
                    (left == True or right == True) and is_p_or_q
                ):
                    return node

                return is_p_or_q or left or right

            node = dfs(root)

            return node

        return Solution3(root, p, q)
