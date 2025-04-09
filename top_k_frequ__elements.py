def top_k_elements(nums: list, k: int) -> list:
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    return [item[0] for item in (sorted(seen.items(), key=lambda item: item[1], reverse=True))[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_elements(nums, k))
