def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Multiply by products of all elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


# Test with your example
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]