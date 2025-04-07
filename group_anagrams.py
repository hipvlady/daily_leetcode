def group_anagrams(strs: list) -> list:
    seen = {}

    for s in strs:
        sorted_s = ''.join(sorted(s, key=str.lower))

        if sorted_s in seen:
            seen[sorted_s].append(s)
        else:
            seen[sorted_s] = [s]

    return [v for v in seen.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
