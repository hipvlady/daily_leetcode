def reverseVowels(s: str) -> str:
    chars = list(s)

    left = 0
    right = len(chars) - 1

    def is_vowel(char):
        return char.lower() in 'aeiou'


    while left < right:
        while left < right and not is_vowel(chars[left]):
            left += 1

        while left < right and not is_vowel(chars[right]):
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]

            left += 1
            right -= 1

    return ''.join(chars)