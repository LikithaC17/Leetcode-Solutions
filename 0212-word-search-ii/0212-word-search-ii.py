class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"

            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = ch

            if not nxt.children:
                del node.children[ch]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return ans