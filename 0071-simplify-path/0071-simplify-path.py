class Solution:
    def simplifyPath(self, path: str) -> str:
        fileName = []
        take = ""
        count = 0
        for paths in path.split("/"):
            if not paths:
                continue
            elif paths == "..":
                if fileName:
                    fileName.pop()
            elif paths != ".":
                fileName.append(paths)
        return "/"+"/".join(fileName)