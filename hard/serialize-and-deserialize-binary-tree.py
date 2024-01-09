# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # dfs inorder transversal

        string = [""]
        def dfs(node):
            
            if not node:
                string[0] += '#' + ","
                return None

            string[0] += str(node.val) + ","
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return string[0]
        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # dfs in order transveral, similar to the serialize() function

        if data == "":
            return None
        
        array = data.split(',')

        if array[0] == '#':
            return None
    
        i = [0]
        def dfs(node):
            
            if array[i[0]] == '#':
                i[0] += 1
                return None

            node.val = int(array[i[0]])
            i[0] += 1
            
            node.left = dfs(TreeNode())
            node.right = dfs(TreeNode())

            return node
        
        root = TreeNode(int(array[0]))
        dfs(root)

        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))