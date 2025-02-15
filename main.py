from api import app
from agents.human_trader import HumanTrader
from agents.manipulative_trader import ManipulativeTrader
from agents.cooperative_trader import CooperativeTrader
from config import CONFIG
import threading

# Initialize traders
human_trader = HumanTrader("HumanTrader", CONFIG["market"]["initial_balance"])
manipulative_trader = ManipulativeTrader("ManipulativeTrader", CONFIG["market"]["initial_balance"])
cooperative_trader = CooperativeTrader("CooperativeTrader", CONFIG["market"]["initial_balance"])

traders = [human_trader, manipulative_trader, cooperative_trader]

def simulate_market():
    market_state = {"AAPL": 100, "TSLA": 200}  # Example market prices
    for trader in traders:
        decision = trader.decide_trade(market_state)
        print(f"{trader.name} decision: {decision}")

if __name__ == "__main__":
    # Start API in a separate thread
    threading.Thread(target=app.run, kwargs={"debug": True}).start()
    
    # Run market simulation
    simulate_market()
