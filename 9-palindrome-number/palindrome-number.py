class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if (x < 0):
            return False
        if (x == 0):
            return True
        while (x > 0):    
            while (x!=0):
                r = x % 10
                rev = rev * 10 + r
                x =  x // 10
            if (temp == rev):
                return True
            else:
                return False       