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


# Lets think about the logic behind the code.
# as in any case we are gonna define class and here the class is proft since thats the  main thing
# then we are going to define the stuff we need for it so self is used which is always used and the prices
# for all this to happen we are going to buy and so for buy the prices default or min needs to be zero
# as we are figuring out profit then profit also needs to be defined hence profit is defined as 0
# we are gonna use for loop to iterate through the prices and check if the price is less than the buy price then we are going to update the buy price
# i is used and a range is set where 1, len i.e length of price will be checked
# if price is less than buy then it is updated and buy ois equal to price
# else if is ginna be used and if price - profit is greater than buy then profit is updated and profit is equal to price - buy
# and profit is retuened
