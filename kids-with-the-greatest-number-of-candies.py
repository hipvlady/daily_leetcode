def kids(candies, extraCandies):
    n = len(candies)
    ans = [False] * n

    max_candies = max(candies)

    for i in range(n):
        if candies[i] + extraCandies >= max_candies:
            ans[i] = True
        else:
            ans[i] = False

    return ans


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kids(candies, extraCandies))