from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        if radiant:
            return "Radiant"
        return "Dire"