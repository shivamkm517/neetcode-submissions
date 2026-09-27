class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l+1, r) or is_palindrome(l, r-1)

            l += 1
            r -= 1
        return True

                