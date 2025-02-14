CONFIG = {
    "market": {
        "initial_balance": 10000,
        "trading_fee": 0.01,
        "risk_tolerance": {
            "rational": 0.5,
            "manipulative": 0.8,
            "cooperative": 0.3
        }
    },
    "deepseek_api": {
        "endpoint": "http://localhost:5000/api",
        "model": "deepseek-r1"
    },
    "reinforcement_learning": {
        "learning_rate": 0.1,
        "discount_factor": 0.9,
        "exploration_rate": 1.0,
        "decay_rate": 0.99
    }
}


if __name__ == "__main__":
    print("Market initial balance:", CONFIG["market"]["initial_balance"])
