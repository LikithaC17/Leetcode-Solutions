class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in word1:
            count1[ord(ch) - ord('a')] += 1

        for ch in word2:
            count2[ord(ch) - ord('a')] += 1

        if any((count1[i] == 0) != (count2[i] == 0) for i in range(26)):
            return False

        return sorted(count1) == sorted(count2)