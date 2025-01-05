import pytest
import gymnasium as gym
import numpy as np
from evorl.environments import NormalizedEnv

@pytest.fixture
def env():
    return NormalizedEnv(gym.make('CartPole-v1'))

def test_normalized_env_initialization(env):
    assert hasattr(env, 'obs_rms')
    assert hasattr(env, 'ret_rms')

def test_normalized_env_step(env):
    obs, _ = env.reset()
    action = env.action_space.sample()
    next_obs, reward, done, truncated, info = env.step(action)
    
    assert isinstance(next_obs, np.ndarray)
    assert isinstance(reward, float)
    assert isinstance(done, bool)
    assert isinstance(truncated, bool)
    assert isinstance(info, dict) 