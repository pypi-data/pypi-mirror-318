from typing import List, Type
import numpy as np
from ..agents.base import Agent

class Population:
    """Manages a population of agents."""
    
    def __init__(self, agent_class: Type[Agent], state_dim: int, action_dim: int, population_size: int = 10):
        self.population = [
            agent_class(state_dim, action_dim)
            for _ in range(population_size)
        ]
        self.fitness_scores = np.zeros(population_size) 