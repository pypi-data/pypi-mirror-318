"""
EvoRL: Evolutionary Reinforcement Learning Framework
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("evorl")
except PackageNotFoundError:
    __version__ = "0.1.2.dev0"

# Import core components
from .agents.base import Agent
from .agents.dqn import DQNAgent
from .agents.ppo import PPOAgent

# Import evolution components
from .evolution.population import Population
from .evolution.strategies import (
    EvolutionStrategy,
    CEM,
    PGPE,
    NES
)

# Import environment components
from .environments.wrappers import NormalizedEnv

__all__ = [
    # Agents
    "Agent",
    "DQNAgent",
    "PPOAgent",
    
    # Evolution
    "Population",
    "EvolutionStrategy",
    "CEM",
    "PGPE",
    "NES",
    
    # Environments
    "NormalizedEnv",
] 