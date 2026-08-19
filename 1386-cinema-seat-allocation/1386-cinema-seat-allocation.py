class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats using a bitmask
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0
            rows[row] |= (1 << seat)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))) == 0
            middle = (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))) == 0
            right = (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9))) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans