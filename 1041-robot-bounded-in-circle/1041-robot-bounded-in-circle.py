class Solution(object):
    def isRobotBounded(self, instructions):
        x = 0
        y = 0
        direction = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for move in instructions:
            if move == 'G':
                x += dx[direction]
                y += dy[direction]
            elif move == 'L':
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0