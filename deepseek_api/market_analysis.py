from deepseek_api.deepseek_client import DeepseekClient

class MarketAnalysis:
    def __init__(self):
        self.client = DeepseekClient()

    def analyze_market(self, historical_data):
        prompt = f"""
        Given the following market data: {historical_data}, 
        what are the expected trends and possible investment strategies?
        """
        return self.client.query(prompt)
