import time
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime
import json
import os
import numpy as np
from collections import defaultdict

@dataclass
class ExperimentConfig:
    """Configuration for an experiment."""
    name: str
    agent_type: str
    env_name: str
    population_size: int
    generations: int
    strategy: str
    seed: int
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return {
            'name': self.name,
            'agent_type': self.agent_type,
            'env_name': self.env_name,
            'population_size': self.population_size,
            'generations': self.generations,
            'strategy': self.strategy,
            'seed': self.seed,
            'timestamp': self.timestamp
        }

class ExperimentLogger:
    """Logger for evolutionary training experiments."""
    
    def __init__(
        self,
        config: ExperimentConfig,
        log_dir: str = "logs",
        log_frequency: int = 1
    ):
        """Initialize logger.
        
        Args:
            config: Experiment configuration
            log_dir: Directory to save logs
            log_frequency: How often to log metrics (in generations)
        """
        self.config = config
        self.log_frequency = log_frequency
        
        # Create log directory
        self.exp_dir = os.path.join(
            log_dir,
            f"{config.name}_{config.timestamp}"
        )
        os.makedirs(self.exp_dir, exist_ok=True)
        
        # Save config
        with open(os.path.join(self.exp_dir, "config.json"), "w") as f:
            json.dump(config.to_dict(), f, indent=4)
        
        # Initialize metrics
        self.metrics = defaultdict(list)
        self.generation = 0
        self.start_time = time.time()
    
    def log_generation(
        self,
        fitness_scores: np.ndarray,
        agent_metrics: List[Dict[str, float]],
        extra_metrics: Optional[Dict[str, Any]] = None
    ) -> None:
        """Log metrics for current generation.
        
        Args:
            fitness_scores: Array of fitness scores for population
            agent_metrics: List of metric dictionaries from agents
            extra_metrics: Additional metrics to log
        """
        if self.generation % self.log_frequency != 0:
            self.generation += 1
            return
        
        # Log fitness statistics
        self.metrics['gen_mean_fitness'].append(float(np.mean(fitness_scores)))
        self.metrics['gen_max_fitness'].append(float(np.max(fitness_scores)))
        self.metrics['gen_min_fitness'].append(float(np.min(fitness_scores)))
        self.metrics['gen_std_fitness'].append(float(np.std(fitness_scores)))
        
        # Log mean agent metrics
        for key in agent_metrics[0].keys():
            mean_value = np.mean([m[key] for m in agent_metrics])
            self.metrics[f'mean_{key}'].append(float(mean_value))
        
        # Log extra metrics
        if extra_metrics:
            for key, value in extra_metrics.items():
                self.metrics[key].append(value)
        
        # Log timing
        elapsed = time.time() - self.start_time
        self.metrics['wall_time'].append(elapsed)
        
        # Save metrics
        self._save_metrics()
        self.generation += 1
    
    def _save_metrics(self) -> None:
        """Save metrics to disk."""
        metrics_path = os.path.join(self.exp_dir, "metrics.json")
        with open(metrics_path, "w") as f:
            json.dump(self.metrics, f, indent=4) 