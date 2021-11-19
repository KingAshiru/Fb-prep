class Solution:
    def decodeString(self, s: str) -> str:
        cur_string, cur_num = "", 0
        stack = []
        
        for char in s:
            if char == '[':
                stack.append(cur_num)
                stack.append(cur_string)
                cur_string, cur_num = "", 0
            elif char == ']':
                string = stack.pop()
                num = stack.pop()
                cur_string = string + cur_string * int(num)
            elif char.isdigit():
                cur_num = 10 * cur_num + int(char)
            else:
                cur_string += char
        
        return cur_string
