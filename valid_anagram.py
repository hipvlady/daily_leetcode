

def valid_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False

    letters = [0] * 26

    for c in s:
        index = ord(c) - ord('a')
        letters[index] += 1

    for char in t:
        index = ord(char) - ord('a')
        letters[index] -= 1

    return not any(x != 0 for x in letters)


s = "anagram"
t = "nagaram"
result = valid_anagram(s,t)
print(result)

