class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    solution = Solution()
    for test in tests:
        print(test, "->", solution.isValid(test))
