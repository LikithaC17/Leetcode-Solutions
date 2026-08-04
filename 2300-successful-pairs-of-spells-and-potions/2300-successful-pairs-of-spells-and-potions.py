from bisect import bisect_left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            need = (success + spell - 1) // spell  
            idx = bisect_left(potions, need)
            ans.append(m - idx)

        return ans