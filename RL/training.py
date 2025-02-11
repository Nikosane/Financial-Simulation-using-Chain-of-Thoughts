import random
import numpy as np

class RLTrader:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0):
        self.actions = actions
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)  # Explore
        return max(self.actions, key=lambda action: self.q_table.get((state, action), 0))  # Exploit

    def update_q_table(self, state, action, reward, next_state):
        old_value = self.q_table.get((state, action), 0)
        future_value = max([self.q_table.get((next_state, a), 0) for a in self.actions], default=0)
        new_value = old_value + self.learning_rate * (reward + self.discount_factor * future_value - old_value)
        self.q_table[(state, action)] = new_value

    def decay_exploration(self, decay_rate=0.99):
        self.exploration_rate *= decay_rate

# Example usage
if __name__ == "__main__":
    actions = ["buy", "sell", "hold"]
    trader = RLTrader(actions)
    print("Initialized RL Trader")
