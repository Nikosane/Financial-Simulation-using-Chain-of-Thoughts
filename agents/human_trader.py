from agents.trader_base import TraderBase

class HumanTrader(TraderBase):
    def decide_trade(self, market_state):
        decision = "hold"
        for asset, price in market_state.items():
            if price < 50:  
                decision = f"buy {asset}"
            elif price > 150:  
                decision = f"sell {asset}"
        return decision


if __name__ == "__main__":
    trader = HumanTrader("RationalTrader", 1000)
    market_state = {"AAPL": 45, "TSLA": 200}
    print(trader.decide_trade(market_state))
