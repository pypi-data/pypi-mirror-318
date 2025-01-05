# EvoRL

An evolutionary reinforcement learning framework that combines evolutionary algorithms with deep RL.

## Installation

```bash
pip install evorl
```

## Quick Start

```python
from evorl import DQNAgent, Population, CEM, NormalizedEnv
import gymnasium as gym

# Create environment
env = NormalizedEnv(gym.make("CartPole-v1"))

# Create population of agents
population = Population(
    agent_class=DQNAgent,
    state_dim=env.observation_space.shape[0],
    action_dim=env.action_space.n,
    population_size=10
)

# Create evolution strategy
strategy = CEM(elite_frac=0.2)
```

## Features

- 🧬 Evolutionary optimization of RL agents
- 🤖 Multiple agent types (DQN, PPO)
- 🔄 Various evolution strategies (CEM, PGPE, NES)
- 📊 Environment normalization and preprocessing
- 🚀 Easy to extend and customize

## Development

```bash
# Clone the repository
git clone https://github.com/zhangalex1/evorl.git
cd evorl

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/
```

## License

MIT License 