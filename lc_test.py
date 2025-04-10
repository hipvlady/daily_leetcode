def fn(a: list[int]) -> list[int]:
    n = len(a)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= a[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= a[i]

    return answer


arr = [1, 2, 3, 4]
print(fn(arr))
