class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = []
        for c in s:
            if c == "(":
                stack.append(cur)
                cur = []
            elif c == ")":
                cur.reverse()
                cur = stack.pop() + cur
            else:
                cur.append(c)
        return "".join(cur)