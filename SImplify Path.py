class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathList = path.split("/")
        
        for dir_ in pathList:
            if dir_ == "..":
                if stack:
                    stack.pop()
            elif dir_ == "." or not dir_:
                continue
            else:
                stack.append(dir_)
        
        return "/" + "/".join(stack)
