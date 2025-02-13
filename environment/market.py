class Market:
    def __init__(self):
        self.prices = {}
        self.history = []

    def update_price(self, asset, new_price):
        self.prices[asset] = new_price
        self.history.append((asset, new_price))

    def get_price(self, asset):
        return self.prices.get(asset, None)

    def get_market_state(self):
        return self.prices


if __name__ == "__main__":
    market = Market()
    market.update_price("AAPL", 150)
    print(market.get_market_state())
