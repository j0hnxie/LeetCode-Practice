class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_len, cur_words = 0, []

        lines = []
        for word in words:
            cur_words.append(word + " ")
            cur_len += len(word) + 1
            if cur_len - 1 > maxWidth:
                cur_words.pop()
                cur_len -= len(word) + 1

                spaces = maxWidth - (cur_len - 1)
                groups = len(cur_words) - 1

                if groups == 0:
                    line = cur_words[0] + " " * spaces
                else:
                    spaces_per_group = spaces // groups
                    extra_spaces = spaces % groups
                    print(spaces)
                    print(groups)
                    line = ""
                    for idx in range(groups):
                        line += cur_words[idx]
                        line += " " * spaces_per_group
                        if idx < extra_spaces:
                            line += " "
                    line += cur_words[-1]

                lines.append(line[:-1])

                cur_len, cur_words = len(word) + 1, [word + " "]
        
                spaces = maxWidth - (cur_len - 1)
                groups = len(cur_words) - 1

        line = "".join(cur_words)
        spaces = maxWidth - (len(line) - 1)
        line += " " * spaces
        lines.append(line[:-1])
        return lines