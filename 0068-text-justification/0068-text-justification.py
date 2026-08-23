class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line = []
            line_len = 0

           
            while i < n and line_len + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1

           
            if i == n or len(line) == 1:
                text = " ".join(line)
                text += " " * (maxWidth - len(text))
                res.append(text)
            else:
                spaces = maxWidth - line_len
                gaps = len(line) - 1

                even = spaces // gaps
                extra = spaces % gaps

                text = ""
                for j in range(gaps):
                    text += line[j]
                    text += " " * (even + (1 if j < extra else 0))
                text += line[-1]
                res.append(text)

        return res