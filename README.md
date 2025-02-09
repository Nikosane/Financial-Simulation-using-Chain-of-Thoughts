# Financial-Simulation-using-Chain-of-Thoughts

## Overview
This project simulates an AI-driven financial market where traders use Chain of Thought (CoT) reasoning to predict market movements, manipulate prices, and make strategic trades. It encourages emergent behaviors such as deception, cooperation, and strategic decision-making. The project is powered by Reinforcement Learning and integrates Deepseek R1 1.5B via Ollama for advanced decision-making.

## Features
- **AI Traders**: Different agent types including rational, manipulative, and cooperative traders.
- **Market Simulation**: A local financial market with an order book and economic model.
- **Deepseek API Integration**: AI-powered market analysis and trader decision-making.
- **Reinforcement Learning**: Agents learn and optimize trading strategies over time.
- **REST API**: Exposes endpoints for real-time market insights and trade execution.

## Installation
### Prerequisites
- Python 3.8+
- Ollama installed with Deepseek R1 1.5B downloaded
- Required dependencies

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Nikosane/Financial-Simulation-using-chain-of-thoughts.git
   cd Financial-Simulation-using-chain-of-thoughts
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure Ollama is running and Deepseek is available:
   ```sh
   ollama run deepseek-r1
   ```

## Usage
### Run the Simulation
```sh
python main.py
```

### Start the API Server
```sh
python api.py
```

### API Endpoints
#### Market Analysis
- **Endpoint:** `/analyze_market`
- **Method:** `POST`
- **Payload:** `{ "historical_data": "<market data>" }`
- **Response:** `{ "analysis": "<Deepseek market insight>" }`

#### Trader Decision-Making
- **Endpoint:** `/trade_decision`
- **Method:** `POST`
- **Payload:** `{ "market_state": "<current market>" , "trader_type": "manipulative" }`
- **Response:** `{ "decision": "<Deepseek trading move>" }`

## Next Steps
- Implement market dynamics (`market.py`, `order_book.py`)
- Develop AI trading strategies (`trader_base.py`, `human_trader.py`, etc.)
- Optimize Deepseek prompts for CoT reasoning
- Train reinforcement learning models (`training.py`)
