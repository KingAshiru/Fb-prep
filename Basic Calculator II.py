class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = "+"

        for idx,char in enumerate(s):
            if char.isdigit():
                num = num*10 + int(char)
            if char in "+-/*" or idx==len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(math.trunc(stack.pop()/num))
                num = 0
                sign = char
        return sum(stack)
