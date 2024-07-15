class Solution:
    def simplifyPath(self, path: str) -> str:
        # https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

        # output = "/"
        folders = path.split("/")
        stack = []
        # Use stack to handle ".."
        for i, folder in  enumerate(folders):
            if folder == "" or folders[i] == ".": continue
            if folders[i] == "..": 
                if stack: stack.pop()
                continue
            stack.append(folder)

        return "/" + "/".join(stack)

        # # Convert stack to path string
        # for i, folder in  enumerate(stack):
        #     output += folder + "/"
        
        # output[:-1] if len(output[:-1]) > 0 else "/"

            