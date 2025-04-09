
numbers = [2, 7, 11, 15]
target = 9
left = 0
right = len(numbers) - 1

while left < right:

    print(f"{numbers[left]} - {numbers[right]}")

    if numbers[left] + numbers[right] == target:
        print("Found")

    elif numbers[left] + numbers[right] == target:
        right -= 1
        print(f"{numbers[right]}")
