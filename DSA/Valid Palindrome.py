# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


name1 = "A man, a plan, a canal: Panama"
name2 = "Anna is a mad man"
print(Solution().isPalindrome(name1))
print(Solution().isPalindrome(name2))

# lets understand the logic behind this code
# class is defined here in this case the class is solution with object in brackets
# def the palindrome with self and s as a variable in brackets
