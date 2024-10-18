"""https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=hash-table"""


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict = {}
    arr = []
    for i in range(len(strs)):
        a = sorted(strs[i])
        a = "".join(a)

        if a in dict.keys():
            dict[a].append(strs[i])
        else:
            dict[a] = [strs[i]]
    for i in dict.keys():
        arr.append(dict.get(i))
    print(arr)


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
