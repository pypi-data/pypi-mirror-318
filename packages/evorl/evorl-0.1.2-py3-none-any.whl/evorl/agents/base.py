from abc import ABC, abstractmethod
import torch
import numpy as np
from typing import Dict, Any, Tuple, Optional

class Agent(ABC):
    """Base class for all EvoRL agents."""
    
    def __init__(self, state_dim: int, action_dim: int, config: Optional[Dict[str, Any]] = None):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.config = config or {}
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.metrics = {}
        self.training = True
    
    @abstractmethod
    def select_action(self, state: np.ndarray) -> np.ndarray:
        pass
    
    @abstractmethod
    def update(self, experience: Tuple) -> Dict[str, float]:
        pass 