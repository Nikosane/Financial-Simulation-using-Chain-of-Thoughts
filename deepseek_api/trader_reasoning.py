from deepseek_api.deepseek_client import DeepseekClient

class TraderReasoning:
    def __init__(self):
        self.client = DeepseekClient()

    def get_trading_decision(self, market_state, trader_type):
        prompt = f"""
        You are a {trader_type} AI trader in a financial market. 
        Market State: {market_state}
        What is your next trading move? Explain your reasoning.
        """
        return self.client.query(prompt)
