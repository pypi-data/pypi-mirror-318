import gymnasium as gym
import numpy as np
from typing import Tuple, Dict

class RunningMeanStd:
    """Tracks running mean and standard deviation."""
    
    def __init__(self, shape: Tuple[int, ...]):
        self.mean = np.zeros(shape, dtype=np.float64)
        self.var = np.ones(shape, dtype=np.float64)
        self.count = 0
    
    def update(self, x: np.ndarray) -> None:
        batch_mean = np.mean(x, axis=0)
        batch_var = np.var(x, axis=0)
        batch_count = x.shape[0]
        
        delta = batch_mean - self.mean
        tot_count = self.count + batch_count
        
        new_mean = self.mean + delta * batch_count / tot_count
        m_a = self.var * self.count
        m_b = batch_var * batch_count
        M2 = m_a + m_b + np.square(delta) * self.count * batch_count / tot_count
        new_var = M2 / tot_count
        
        self.mean = new_mean
        self.var = new_var
        self.count = tot_count

class NormalizedEnv(gym.Wrapper):
    """Normalizes observations and rewards."""
    
    def __init__(
        self,
        env: gym.Env,
        clip_obs: float = 10.0,
        clip_reward: float = 10.0,
        gamma: float = 0.99,
        epsilon: float = 1e-8
    ):
        super().__init__(env)
        self.clip_obs = clip_obs
        self.clip_reward = clip_reward
        self.gamma = gamma
        self.epsilon = epsilon
        
        self.obs_rms = RunningMeanStd(shape=self.observation_space.shape)
        self.ret_rms = RunningMeanStd(shape=())
        self.return_acc = 0.0
    
    def step(self, action) -> Tuple[np.ndarray, float, bool, bool, Dict]:
        obs, reward, terminated, truncated, info = self.env.step(action)
        
        self.return_acc = self.return_acc * self.gamma + reward
        self.ret_rms.update(np.array([self.return_acc]))
        
        normalized_obs = self._normalize_obs(obs)
        normalized_reward = self._normalize_reward(reward)
        
        if terminated or truncated:
            self.return_acc = 0.0
        
        return normalized_obs, normalized_reward, terminated, truncated, info
    
    def reset(self, **kwargs) -> Tuple[np.ndarray, Dict]:
        obs, info = self.env.reset(**kwargs)
        self.return_acc = 0.0
        return self._normalize_obs(obs), info
    
    def _normalize_obs(self, obs: np.ndarray) -> np.ndarray:
        """Normalize observations using running statistics."""
        self.obs_rms.update(obs.reshape(1, -1))
        normalized = (obs - self.obs_rms.mean) / np.sqrt(self.obs_rms.var + self.epsilon)
        return np.clip(normalized, -self.clip_obs, self.clip_obs)
    
    def _normalize_reward(self, reward: float) -> float:
        """Normalize rewards using running statistics."""
        normalized = reward / np.sqrt(self.ret_rms.var + self.epsilon)
        return float(np.clip(normalized, -self.clip_reward, self.clip_reward)) 