class TraderBase:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.portfolio = {}
    
    def buy(self, asset, quantity, price):
        cost = quantity * price
        if self.balance >= cost:
            self.balance -= cost
            self.portfolio[asset] = self.portfolio.get(asset, 0) + quantity
            return f"{self.name} bought {quantity} of {asset}"
        return "Insufficient balance"
    
    def sell(self, asset, quantity, price):
        if self.portfolio.get(asset, 0) >= quantity:
            self.portfolio[asset] -= quantity
            self.balance += quantity * price
            return f"{self.name} sold {quantity} of {asset}"
        return "Not enough assets to sell"
    
    def get_portfolio_value(self, market_prices):
        value = self.balance + sum(self.portfolio[asset] * market_prices.get(asset, 0) for asset in self.portfolio)
        return value
    
    def decide_trade(self, market_state):
        raise NotImplementedError("This method should be implemented by subclasses")


if __name__ == "__main__":
    trader = TraderBase("BaseTrader", 1000)
    print(trader.buy("AAPL", 5, 150))
