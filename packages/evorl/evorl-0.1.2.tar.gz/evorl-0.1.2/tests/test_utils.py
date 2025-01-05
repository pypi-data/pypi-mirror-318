import pytest
import numpy as np
import os
from evorl.utils.logging import ExperimentConfig, ExperimentLogger
from evorl.utils.visualization import plot_training_curves, plot_population_distribution

def test_experiment_config():
    config = ExperimentConfig(
        name="test_exp",
        agent_type="DQN",
        env_name="CartPole-v1",
        population_size=10,
        generations=50,
        strategy="CEM",
        seed=42
    )
    
    assert config.name == "test_exp"
    assert config.agent_type == "DQN"
    config_dict = config.to_dict()
    assert isinstance(config_dict, dict)
    assert "timestamp" in config_dict

def test_experiment_logger(tmp_path):
    config = ExperimentConfig(
        name="test_exp",
        agent_type="DQN",
        env_name="CartPole-v1",
        population_size=10,
        generations=50,
        strategy="CEM",
        seed=42
    )
    
    logger = ExperimentLogger(config, log_dir=str(tmp_path))
    
    # Test logging
    fitness_scores = np.array([1.0, 2.0, 3.0])
    agent_metrics = [{'loss': 0.1} for _ in range(3)]
    logger.log_generation(fitness_scores, agent_metrics)
    
    assert os.path.exists(os.path.join(logger.exp_dir, "metrics.json")) 