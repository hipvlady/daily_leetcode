def max_profit(prices):
    if len(prices) <= 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)

        min_price = min(min_price, price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
