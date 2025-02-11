def reward_function(trader_type, profit, risk_taken):
    if trader_type == "rational":
        return profit - risk_taken * 0.5  # Balanced risk-reward
    elif trader_type == "manipulative":
        return profit * 1.2 if risk_taken > 0.7 else profit * 0.8  # Encourages high-risk behavior
    elif trader_type == "cooperative":
        return profit + (0.2 * risk_taken)  # Rewards cooperation while considering risk
    else:
        return profit  # Default case

# Example usage
if __name__ == "__main__":
    print(reward_function("rational", 100, 0.4))  # Expected reward output
