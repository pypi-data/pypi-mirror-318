import pytest
import torch
import numpy as np
from evorl import DQNAgent

@pytest.fixture
def state_dim():
    return 4

@pytest.fixture
def action_dim():
    return 2

def test_dqn_agent_initialization(state_dim, action_dim):
    agent = DQNAgent(state_dim, action_dim)
    assert agent.state_dim == state_dim
    assert agent.action_dim == action_dim
    assert isinstance(agent.device, torch.device)

def test_dqn_agent_action_selection(state_dim, action_dim):
    agent = DQNAgent(state_dim, action_dim)
    state = np.random.randn(state_dim)
    action = agent.select_action(state)
    assert isinstance(action, np.ndarray)
    assert action.shape == () or action.shape == (1,)
    assert 0 <= action < action_dim 