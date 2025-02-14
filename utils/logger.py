import logging


logging.basicConfig(
    filename='market_activity.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_trade(trader_name, action, asset, quantity, price):
    message = f"{trader_name} {action} {quantity} of {asset} at {price}"
    logging.info(message)

def log_decision(trader_name, decision):
    logging.info(f"{trader_name} decision: {decision}")

def log_error(error_message):
    logging.error(error_message)


if __name__ == "__main__":
    log_trade("Trader1", "bought", "AAPL", 10, 150)
    log_decision("Trader1", "buy AAPL")
    log_error("Insufficient balance error")
