'''
Complexity Analysis

Time Complexity: O(n),This is because we are iterating through the array of prices exactly once. 
               > There are no nested loops or recursive calls.

Space Complexity: O(1),Only two variables are used to store the minimum price and maximum profit, regardless of the input size.
'''

# Function to calculate maximum profit using single pass
def stockbuySell(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:

        # If current price is less than min_price, update min_price
        if price < min_price:
            min_price = price

        # Else calculate profit and update max_profit if it's greater
        else:
            max_profit = max(max_profit, price - min_price)

    # Return the maximum profit found
    return max_profit

prices = list(map(int, input("Enter the prices (space-separated): ").split()))
print("Max Profit:", stockbuySell(prices))