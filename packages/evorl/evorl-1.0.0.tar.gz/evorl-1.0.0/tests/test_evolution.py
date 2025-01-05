import pytest
import numpy as np
from evorl import Population, CEM, DQNAgent

@pytest.fixture
def population_params():
    return {
        'agent_class': DQNAgent,
        'state_dim': 4,
        'action_dim': 2,
        'population_size': 5
    }

def test_population_initialization(population_params):
    population = Population(**population_params)
    assert len(population.population) == population_params['population_size']
    assert all(isinstance(agent, population_params['agent_class']) for agent in population.population)

def test_cem_strategy():
    strategy = CEM(elite_frac=0.2)
    agents = [DQNAgent(4, 2) for _ in range(5)]
    fitness_scores = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    
    updates = strategy.compute_updates(agents, fitness_scores)
    assert len(updates) == len(agents)
    assert all(isinstance(update, dict) for update in updates) 