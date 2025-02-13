class Economy:
    def __init__(self, growth_rate=0.02, inflation_rate=0.03):
        self.growth_rate = growth_rate
        self.inflation_rate = inflation_rate
        self.market_conditions = {}

    def update_conditions(self, new_growth, new_inflation):
        self.growth_rate = new_growth
        self.inflation_rate = new_inflation
        self.market_conditions["growth"] = self.growth_rate
        self.market_conditions["inflation"] = self.inflation_rate

    def get_conditions(self):
        return self.market_conditions


if __name__ == "__main__":
    economy = Economy()
    economy.update_conditions(0.025, 0.035)
    print(economy.get_conditions())
