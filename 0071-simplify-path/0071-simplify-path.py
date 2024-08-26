class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")

        stack = []
        for directory in dirs:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or directory == "":
                continue
            else:
                stack.append(directory)
        
        res = "/" + "/".join(stack)
        return res
