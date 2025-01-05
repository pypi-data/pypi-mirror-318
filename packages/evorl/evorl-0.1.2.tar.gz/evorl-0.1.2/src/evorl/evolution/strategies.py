from abc import ABC, abstractmethod
from typing import List, Dict
import numpy as np
import torch
from ..agents.base import Agent

class EvolutionStrategy(ABC):
    """Base class for evolution strategies."""
    
    @abstractmethod
    def compute_updates(self, agents: List[Agent], fitness_scores: np.ndarray) -> List[Dict[str, torch.Tensor]]:
        pass

class CEM(EvolutionStrategy):
    """Cross-Entropy Method."""
    
    def __init__(self, elite_frac: float = 0.2):
        self.elite_frac = elite_frac
    
    def compute_updates(self, agents: List[Agent], fitness_scores: np.ndarray) -> List[Dict[str, torch.Tensor]]:
        return [{}] * len(agents)  # Placeholder 

class PGPE(EvolutionStrategy):
    """Policy Gradients with Parameter-Based Exploration."""
    
    def __init__(self, learning_rate: float = 0.01, noise_std: float = 0.1):
        self.learning_rate = learning_rate
        self.noise_std = noise_std
        self.mean_params = None
    
    def compute_updates(self, agents: List[Agent], fitness_scores: np.ndarray) -> List[Dict[str, torch.Tensor]]:
        # Initialize mean parameters if not already done
        if self.mean_params is None:
            self.mean_params = {}
            for key, value in agents[0].state_dict().items():
                if isinstance(value, torch.Tensor):
                    self.mean_params[key] = value.clone()
        
        # Normalize fitness scores
        fitness_scores = (fitness_scores - fitness_scores.mean()) / (fitness_scores.std() + 1e-8)
        
        # Generate new parameters
        updates = []
        for _ in range(len(agents)):
            update = {}
            for key in self.mean_params:
                noise = torch.randn_like(self.mean_params[key]) * self.noise_std
                update[key] = self.mean_params[key] + noise
            updates.append(update)
        
        return updates

class NES(EvolutionStrategy):
    """Natural Evolution Strategies."""
    
    def __init__(self, learning_rate: float = 0.01, noise_std: float = 0.1):
        self.learning_rate = learning_rate
        self.noise_std = noise_std
        self.mean_params = None
    
    def compute_updates(self, agents: List[Agent], fitness_scores: np.ndarray) -> List[Dict[str, torch.Tensor]]:
        # Initialize mean parameters if not already done
        if self.mean_params is None:
            self.mean_params = {}
            for key, value in agents[0].state_dict().items():
                if isinstance(value, torch.Tensor):
                    self.mean_params[key] = value.clone()
        
        # Normalize fitness scores
        fitness_scores = (fitness_scores - fitness_scores.mean()) / (fitness_scores.std() + 1e-8)
        
        # Generate new parameters
        updates = []
        for _ in range(len(agents)):
            update = {}
            for key in self.mean_params:
                noise = torch.randn_like(self.mean_params[key]) * self.noise_std
                update[key] = self.mean_params[key] + noise
            updates.append(update)
        
        return updates 