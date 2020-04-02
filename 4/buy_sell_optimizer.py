def buy_sell_optimizer(stock_prices):
    """Find the best pair of days to buy and sell stocks in order to maximize trading profit,
    assuming that one must buy before selling.

    Parameters:
    stock_prices (list): A list of key-value pairs describing a trading day and price.
    """
    min_entry = stock_prices[0]
    max_entry = stock_prices[1]
    profit = max_entry['Price'] - min_entry['Price']

    for i in range(1, len(stock_prices)): 
        candidate = stock_prices[i]
        # determine if the candidate should be the new min_entry
        if candidate['Price'] < min_entry['Price']: 
            # set candidate to min_entry only if a new max exists for greater profit
            for j in range(i + 1, len(stock_prices)):
                max_cand = stock_prices[j]
                if max_cand['Price'] - candidate['Price'] > profit:
                    min_entry = candidate
                    max_entry = max_cand
                    profit = max_cand['Price'] - candidate['Price']
        # determine if the candidate should be the new max_entry
        elif candidate['Price'] > max_entry['Price']:
            max_entry = candidate

    return f"Buy[%d]Sell[%d]" % (min_entry['Day'], max_entry['Day'])

if __name__ == '__main__':
    stock_prices = [{ "Day": 0, "Price": 5 },
                    { "Day": 1, "Price": 9 },
                    { "Day": 2, "Price": 3 },
                    { "Day": 3, "Price": 5 },
                    { "Day": 4, "Price": 8 },
                    { "Day": 5, "Price": 7 }]
    
    print(buy_sell_optimizer(stock_prices))