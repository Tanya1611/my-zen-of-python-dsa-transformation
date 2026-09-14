# Function to calculate maximum profit using brute force
def stockbuySell(prices):
    
    maxProfit = 0

    # Loop through each day as potential buy day
    for i in range(len(prices)):

        # Loop through future days as potential sell day
        for j in range(i + 1, len(prices)):

            # Calculate profit
            profit = prices[j] - prices[i]

            # Update max profit if higher
            maxProfit = max(maxProfit, profit)

    # Return the maximum profit
    return maxProfit


prices = list(map(int, input("Enter the prices (space-separated): ").split()))
print("Max Profit:", stockbuySell(prices))