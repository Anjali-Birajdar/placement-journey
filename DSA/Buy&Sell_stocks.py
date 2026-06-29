class Profit:
    def MaxProfit(self, prices):
        buy = prices[0]  # [0] is used because we are initialising it
        profit = 0  # 0 because it needs to min that
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - profit > buy:
                profit = prices[i] - buy
        return profit
