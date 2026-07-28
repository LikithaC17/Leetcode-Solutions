class Solution(object):
    def smallestPalindrome(self, s):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        left = []

        for i in range(26):
            left.append(chr(i + ord('a')) * (count[i] // 2))

        left = ''.join(left)

        middle = ''
        for i in range(26):
            if count[i] % 2 == 1:
                middle = chr(i + ord('a'))
                break

        return left + middle + left[::-1]