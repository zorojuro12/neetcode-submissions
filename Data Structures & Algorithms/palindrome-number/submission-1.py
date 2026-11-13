class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0

        if x < 0:
            return False

        num = x
        while num:
            rev = (rev * 10) + (num % 10)
            num = num // 10

        return x == rev
