def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    # s_cleaned = ''.join(ch for ch in s.lower() if ch.isalnum())

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
