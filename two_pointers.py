def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        # Add the current element to our running sum
        current_sum += nums[right]
        
        # Try to minimize the window by moving left pointer
        while current_sum >= target:
            # Update minimum length
            min_length = min(min_length, right - left + 1)
            
            # Remove leftmost element and move left pointer
            current_sum -= nums[left]
            left += 1
    
    # If min_length is still infinity, no valid subarray was found
    return min_length if min_length != float('inf') else 0


target = 7, nums = [2,3,1,2,4,3]
result =minSubArrayLen(target, nums)
print(result)