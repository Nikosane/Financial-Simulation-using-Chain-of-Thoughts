import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class RLModel:
    def __init__(self, input_shape, output_shape, learning_rate=0.001):
        self.model = Sequential([
            Dense(64, activation='relu', input_shape=input_shape),
            Dense(64, activation='relu'),
            Dense(output_shape, activation='linear')
        ])
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')

    def predict(self, state):
        return self.model.predict(np.array([state]))[0]

    def train(self, states, q_values):
        self.model.fit(np.array(states), np.array(q_values), epochs=1, verbose=0)

# Example usage
if __name__ == "__main__":
    model = RLModel(input_shape=(10,), output_shape=3)
    print("Initialized RL Model")
