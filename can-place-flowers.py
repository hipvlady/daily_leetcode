def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    i = 0
    length = len(flowerbed)

    while i < length:
        if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == length - 1 or flowerbed[i + 1] == 0)):

            flowerbed[i] = 1
            count += 1

            i += 2
        else:
            i += 1

        if count >= n:
            return True

    return count >= n