import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import Dict, Any, Tuple, List, Optional
import gymnasium.spaces as spaces

from .base import Agent

class PPONetwork(nn.Module):
    """Combined actor-critic network for PPO."""
    
    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dims: List[int] = [256, 256],
        activation: str = 'tanh'
    ):
        """Initialize the network.
        
        Args:
            state_dim: Dimension of state space
            action_dim: Dimension of action space
            hidden_dims: List of hidden layer dimensions
            activation: Activation function to use
        """
        super().__init__()
        
        # Select activation function
        if activation == 'tanh':
            act_fn = nn.Tanh
        elif activation == 'relu':
            act_fn = nn.ReLU
        else:
            raise ValueError(f"Unsupported activation: {activation}")
        
        # Build shared layers
        layers = []
        prev_dim = state_dim
        
        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                act_fn()
            ])
            prev_dim = hidden_dim
        
        self.shared = nn.Sequential(*layers)
        
        # Policy head (mean and log_std for continuous actions)
        self.policy_mean = nn.Linear(prev_dim, action_dim)
        self.policy_log_std = nn.Parameter(torch.zeros(action_dim))
        
        # Value head
        self.value = nn.Linear(prev_dim, 1)
        
        # Initialize weights
        self.apply(self._init_weights)
    
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            nn.init.orthogonal_(module.weight, gain=np.sqrt(2))
            nn.init.zeros_(module.bias)
    
    def forward(self, state: torch.Tensor) -> Tuple[torch.distributions.Normal, torch.Tensor]:
        """Forward pass through the network.
        
        Args:
            state: Input state tensor
            
        Returns:
            Tuple of (action distribution, value estimate)
        """
        features = self.shared(state)
        
        # Compute action distribution
        mean = self.policy_mean(features)
        std = self.policy_log_std.exp()
        dist = torch.distributions.Normal(mean, std)
        
        # Compute value
        value = self.value(features)
        
        return dist, value

class PPOAgent(Agent):
    """Proximal Policy Optimization agent."""
    
    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        config: Optional[Dict[str, Any]] = None
    ):
        """Initialize PPO agent.
        
        Args:
            state_dim: Dimension of state space
            action_dim: Dimension of action space
            config: Configuration dictionary
        """
        default_config = {
            'learning_rate': 3e-4,
            'gamma': 0.99,
            'gae_lambda': 0.95,
            'clip_ratio': 0.2,
            'hidden_dims': [256, 256],
            'activation': 'tanh',
            'max_grad_norm': 0.5,
            'value_loss_coef': 0.5,
            'entropy_coef': 0.01
        }
        
        config = {**default_config, **(config or {})}
        super().__init__(state_dim, action_dim, config)
        
        # Create network
        self.network = PPONetwork(
            state_dim,
            action_dim,
            config['hidden_dims'],
            config['activation']
        ).to(self.device)
        
        # Create optimizer
        self.optimizer = optim.Adam(self.network.parameters(), lr=config['learning_rate'])
        
        # Initialize metrics
        self.metrics = {
            'policy_loss': 0.0,
            'value_loss': 0.0,
            'entropy': 0.0
        }
    
    def select_action(self, state: np.ndarray) -> np.ndarray:
        """Select an action given the current state."""
        with torch.no_grad():
            state = torch.FloatTensor(state).to(self.device)
            dist, _ = self.network(state)
            
            if self.training:
                action = dist.sample()
            else:
                action = dist.mean
            
            return action.cpu().numpy()
    
    def update(self, experience: Tuple) -> Dict[str, float]:
        """Update the agent using PPO."""
        states, actions, rewards, next_states, dones = experience
        
        # Convert to tensors
        states = torch.FloatTensor(states).to(self.device)
        actions = torch.FloatTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)
        
        # Compute advantages using GAE
        with torch.no_grad():
            _, values = self.network(states)
            _, next_values = self.network(next_states)
            
            advantages = torch.zeros_like(rewards)
            gae = 0
            for t in reversed(range(len(rewards))):
                if t == len(rewards) - 1:
                    next_value = next_values[t]
                else:
                    next_value = values[t + 1]
                
                delta = rewards[t] + self.config['gamma'] * next_value * (1 - dones[t]) - values[t]
                gae = delta + self.config['gamma'] * self.config['gae_lambda'] * (1 - dones[t]) * gae
                advantages[t] = gae
            
            returns = advantages + values
        
        # PPO update
        dist, values = self.network(states)
        log_probs = dist.log_prob(actions).sum(-1)
        entropy = dist.entropy().mean()
        
        # Compute policy loss
        ratio = torch.exp(log_probs - old_log_probs)
        clip_adv = torch.clamp(ratio, 1 - self.config['clip_ratio'], 1 + self.config['clip_ratio']) * advantages
        policy_loss = -torch.min(ratio * advantages, clip_adv).mean()
        
        # Compute value loss
        value_loss = 0.5 * (returns - values.squeeze()).pow(2).mean()
        
        # Total loss
        loss = (
            policy_loss
            + self.config['value_loss_coef'] * value_loss
            - self.config['entropy_coef'] * entropy
        )
        
        # Update network
        self.optimizer.zero_grad()
        loss.backward()
        nn.utils.clip_grad_norm_(self.network.parameters(), self.config['max_grad_norm'])
        self.optimizer.step()
        
        # Update metrics
        self.metrics.update({
            'policy_loss': float(policy_loss.item()),
            'value_loss': float(value_loss.item()),
            'entropy': float(entropy.item())
        })
        
        return self.metrics
    
    def state_dict(self) -> Dict[str, Any]:
        return {
            'network': self.network.state_dict(),
            'optimizer': self.optimizer.state_dict()
        }
    
    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        self.network.load_state_dict(state_dict['network'])
        self.optimizer.load_state_dict(state_dict['optimizer']) 