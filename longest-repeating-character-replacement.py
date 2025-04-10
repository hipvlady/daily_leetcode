def fn(s: str, k: int) -> int:
    n = len(s)
    seen = set()
    left, max_length = 0, 0

    for right in range(n):
        while s[right] in seen and k > 0:
            seen.remove(s[left])
            left += 1
            k -=1

        seen.add(s[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


s = "AABABBA"
k = 1
print(fn(s, k))