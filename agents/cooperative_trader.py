from agents.trader_base import TraderBase

class CooperativeTrader(TraderBase):
    def decide_trade(self, market_state):
        decision = "hold"
        for asset, price in market_state.items():
            if price < 90:  
                decision = f"buy {asset}"
            elif price > 140:  
                decision = f"sell {asset}"
        return decision


if __name__ == "__main__":
    trader = CooperativeTrader("CollaborativeTrader", 1000)
    market_state = {"AAPL": 85, "TSLA": 145}
    print(trader.decide_trade(market_state))
