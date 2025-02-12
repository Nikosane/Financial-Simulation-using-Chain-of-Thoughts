from agents.trader_base import TraderBase

class ManipulativeTrader(TraderBase):
    def decide_trade(self, market_state):
        decision = "hold"
        for asset, price in market_state.items():
            if price < 80: 
                decision = f"buy {asset}"
            elif price > 120:  
                decision = f"sell {asset}"
        return decision


if __name__ == "__main__":
    trader = ManipulativeTrader("DeceptiveTrader", 1000)
    market_state = {"AAPL": 75, "TSLA": 130}
    print(trader.decide_trade(market_state))
