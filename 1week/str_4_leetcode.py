""" https://leetcode.com/problems/text-justification/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        s = " "
        paragraph = []
        curr_s = []
        i = -1
        g = 0
        print(g)

        while i < len(words):
            if i == len(words) - 1:
                paragraph.append(
                    " ".join(curr_s)
                    + " " * (maxWidth - sum([len(x) for x in curr_s]) - len(curr_s) + 1)
                )
                return paragraph

            if (
                sum([len(x) for x in curr_s]) + len(words[i + 1]) + (len(curr_s))
                <= maxWidth
            ):

                curr_s.append(words[i + 1])
                g = sum([len(x) for x in curr_s])
                i += 1
            else:
                if len(curr_s) == 1:
                    s = curr_s[0] + " " * (maxWidth - sum([len(x) for x in curr_s]))

                elif (maxWidth - sum([len(x) for x in curr_s])) % (
                    len(curr_s) - 1
                ) == 0:
                    space = " " * (
                        (maxWidth - sum([len(x) for x in curr_s])) // (len(curr_s) - 1)
                    )
                    s = space.join(curr_s)

                else:
                    space = " " * (
                        (maxWidth - sum([len(x) for x in curr_s])) // (len(curr_s) - 1)
                    )
                    unic = (maxWidth - sum([len(x) for x in curr_s])) % (
                        len(curr_s) - 1
                    )
                    s = (
                        "".join([(curr_s[x] + space + " ") for x in range(0, unic)])
                        + "".join(
                            [curr_s[x] + space for x in range(unic, len(curr_s) - 1)]
                        )
                        + curr_s[-1]
                    )

                    print(s)

                paragraph.append(s)
                curr_s = []

        return paragraph
