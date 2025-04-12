def fn(s:str) -> int:
    arr_s = s.split()
    last_item = arr_s[-1]
    length_of_last_item = len(last_item)

    return length_of_last_item


test_cases = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
for test in test_cases:
    print(fn(test))
