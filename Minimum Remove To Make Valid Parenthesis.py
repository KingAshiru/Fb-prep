class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append([i, "("])
            elif char == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append([i, ")"])
        bad = set()
        for i in range(len(stack)):
            bad.add(stack[i][0])
        word = []
        for i, char in enumerate(s):
            if i not in bad:
                word.append(char)
        return "".join(word)
