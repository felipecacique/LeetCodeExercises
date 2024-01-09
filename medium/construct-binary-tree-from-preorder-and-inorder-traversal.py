# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def Solution1(preorder, inorder):
            # the idea is doing a dfs and combine the information of the preorder to fill the node values, and the inorder to figure it out when we have reach a leaf node and do a return (leaf always come first, then the parent, but if we compare this second inorder value with the parent node value, they must be the same, so we skip it and create the right branch of the tree, repeating the process). 
            # In other words, we will fill the values according to the preorder array, and figure it out the branches accorging to inorder array. In the inorder there will be always th esequence [leaf, node, leaf, node, leaf, node ... node, node, node]. I think i will create and auxiliary array, where it has the information of leaf, and use it to build the tree afterwards


            i = [0]
            j = [0]
            seen = set() # holds all the parents nodes

            def dfs(node, parent_val):
                
                if i[0] >= len(preorder) or j[0] >= len(inorder) or not node: # leaf
                    print(None, i[0], j[0])
                    return None

                if parent_val == inorder[j[0]]: # leaf 
                    print(None, i[0], j[0])
                    j[0] += 1
                    return None
                
                node.val = preorder[i[0]]   # we will create the nodes using the preorder list
                seen.add(node.val)
                i[0] += 1
                print(node.val, i[0], j[0])

                node.left = dfs(TreeNode(), node.val) 

                while j[0] < len(inorder) and inorder[j[0]] in seen: # seen hold the the node parents
                    j[0] += 1 # point to the next leaf, jumping all the parents already seen
                
                # if j[0] < len(inorder) and inorder[j[0]] == parent_val:
                #     j[0] += 1

                node.right = dfs(TreeNode(), node.val)

                if j[0] < len(inorder) and inorder[j[0]] == parent_val:
                    j[0] += 1
            
                # while j[0] < len(inorder) and inorder[j[0]] in seen: # seen hold the the node parents
                #     j[0] += 1 # point to the next leaf, jumping all the parents already seen

                return node

            root = TreeNode()
            dfs(root, None)


            def dfs2(node): # just to print the values
                

                if not node:
                    # print(None)
                    return None
                
                print(node.val)

                dfs2(node.left)
                dfs2(node.right)

                return 

            dfs2(root)

            return root
        


        def Solution2(preorder, inorder):
            # solution got from https://www.youtube.com/watch?v=ihj4IQGZ2zc&ab_channel=NeetCode
            
            # indexes = {}
            # for i, item in enumerate(inorder):
            #     indexes[item] = i

            def dfs(preorder, inorder):
                
                if len(inorder) == 0 or len(preorder) == 0:
                    return None

                root = TreeNode()
                root.val = preorder[0]
                root_index = inorder.index(preorder[0])
                # root_index = indexes[preorder[0]]

                root.left = dfs(preorder[1:root_index+1], inorder[:root_index])
                root.right = dfs(preorder[root_index+1:], inorder[root_index+1:])

                return root


        def Solution3(preorder, inorder):
            # solution got from https://www.youtube.com/watch?v=ihj4IQGZ2zc&ab_channel=NeetCode but using indexes
            
            indexes = {}
            for i, item in enumerate(inorder):
                indexes[item] = i

            m = len(inorder)

            def dfs(a,b, c,d):
                
                if a==b or c==d or a >= m or b > m or c >= m or d > m:
                    return None

                root = TreeNode()
                root.val = preorder[a]
                root_index = indexes[preorder[a]]

                root.left = dfs(a+1, root_index+1, c, root_index)
                root.right = dfs(root_index+1, m, root_index+1, m)

                return root

            return dfs(0,m, 0,m)


        return Solution2(preorder, inorder)
