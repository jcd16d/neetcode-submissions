class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedOpen = closeToOpen = {
            ")": "(", "]": "[", "}": "{"
        }
        for char in s:
            if char in closedOpen:
                if stack and stack[-1] == closedOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False