class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = []

        for directory in path:
            if directory == "..":
                if res:
                    res.pop()
            elif directory == "." or directory == "":
                continue
            else:
                res.append(directory)
        
        return "/" + "/".join(res)