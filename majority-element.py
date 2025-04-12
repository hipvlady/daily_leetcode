def fn(nums):
    majority_element = nums[0]
    count = 1

    for num in nums[1:]:
        if count == 0:
            majority_element = num
            count = 1
        elif num == majority_element:
            count += 1
        else:
            count -= 1

    return majority_element


nums = [2,2,1,1,1,2,2]
print(fn(nums))