def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]

    return strs[0]


test_cases = [["flower","flow","flight"],["dog","racecar","car"]]
for test in test_cases:
    print(longestCommonPrefix(test))