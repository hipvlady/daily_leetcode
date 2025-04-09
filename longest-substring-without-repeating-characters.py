def fn(s: str) -> int:
    n = len(s)
    seen = set()
    max_length = 0
    left = 0

    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


s = "abcabcbb"
print(fn(s))
