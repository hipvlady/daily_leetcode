def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            max_length = max(max_length, current_streak)

    return max_length


print(longestConsecutive([100,4,200,1,3,2]))
