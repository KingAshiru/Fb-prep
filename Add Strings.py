class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        carry = 0
        res = []
        
        while ptr1 >= 0 or ptr2 >= 0:
            x1 = ord(num1[ptr1]) - ord('0') if ptr1 >= 0 else 0
            x2 = ord(num2[ptr2]) - ord('0') if ptr2 >= 0 else 0
            val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(str(val))
            
            ptr1 -= 1
            ptr2 -= 1
        
        if carry:
            res.append(str(carry))
        
        return "".join(res[::-1])
