class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        for c in magazine:
            count[c] = count.get(c, 0) + 1

        for c in ransomNote:
            if count.get(c, 0) == 0:
                return False
            count[c] -= 1

        return True