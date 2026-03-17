prices = [7,6,4,3,1]
maxProfit= 0

# in - 10k loop - 10cr
# in - 10k loop - 10k
# your code
for i in range(0, len(prices)):
    for j in range(i, len(prices)-1):
        if (prices[j] - prices[i] > maxProfit):
            maxProfit = prices[j] - prices[i]

# TC -> O(n^2)
# TC -> O(n)

print(maxProfit)