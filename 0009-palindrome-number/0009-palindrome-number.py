class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digit = 0
        temp = x
        reversed_x = 0
        while temp > 0:
            digit = temp % 10
            reversed_x = reversed_x * 10 + digit
            temp //= 10

        if x == reversed_x:
            return True
        return False