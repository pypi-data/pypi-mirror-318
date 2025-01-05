from typing import Dict, List, Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
from pathlib import Path
import json

def plot_training_curves(
    metrics_file: str,
    save_dir: Optional[str] = None,
    show: bool = True
) -> Tuple[Figure, Figure]:
    """Plot training curves from metrics file.
    
    Args:
        metrics_file: Path to metrics JSON file
        save_dir: Directory to save plots (optional)
        show: Whether to display plots
        
    Returns:
        Tuple of (fitness_fig, metrics_fig)
    """
    # Load metrics
    with open(metrics_file, 'r') as f:
        metrics = json.load(f)
    
    # Create fitness plot
    fitness_fig = plt.figure(figsize=(10, 6))
    plt.plot(metrics['gen_mean_fitness'], label='Mean Fitness')
    plt.plot(metrics['gen_max_fitness'], label='Max Fitness')
    plt.fill_between(
        range(len(metrics['gen_mean_fitness'])),
        np.array(metrics['gen_mean_fitness']) - np.array(metrics['gen_std_fitness']),
        np.array(metrics['gen_mean_fitness']) + np.array(metrics['gen_std_fitness']),
        alpha=0.2
    )
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Population Fitness Over Time')
    plt.legend()
    plt.grid(True)
    
    # Create metrics plot
    metric_keys = [k for k in metrics.keys() if k.startswith('mean_')]
    if metric_keys:
        metrics_fig = plt.figure(figsize=(10, 6))
        for key in metric_keys:
            plt.plot(metrics[key], label=key.replace('mean_', ''))
        plt.xlabel('Generation')
        plt.ylabel('Value')
        plt.title('Agent Metrics Over Time')
        plt.legend()
        plt.grid(True)
    else:
        metrics_fig = None
    
    # Save plots
    if save_dir:
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        fitness_fig.savefig(save_dir / 'fitness.png')
        if metrics_fig:
            metrics_fig.savefig(save_dir / 'metrics.png')
    
    if show:
        plt.show()
    
    return fitness_fig, metrics_fig

def plot_population_distribution(
    fitness_scores: np.ndarray,
    generation: int,
    save_path: Optional[str] = None,
    show: bool = True
) -> Figure:
    """Plot distribution of fitness scores in population.
    
    Args:
        fitness_scores: Array of fitness scores
        generation: Current generation number
        save_path: Path to save plot (optional)
        show: Whether to display plot
        
    Returns:
        Figure object
    """
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(fitness_scores, kde=True)
    plt.xlabel('Fitness Score')
    plt.ylabel('Count')
    plt.title(f'Population Fitness Distribution (Generation {generation})')
    
    if save_path:
        plt.savefig(save_path)
    
    if show:
        plt.show()
    
    return fig

def plot_agent_architecture(
    agent,
    save_path: Optional[str] = None,
    show: bool = True
) -> Figure:
    """Plot neural network architecture of an agent.
    
    Args:
        agent: Agent instance
        save_path: Path to save plot (optional)
        show: Whether to display plot
        
    Returns:
        Figure object
    """
    # Get network structure
    layers = []
    for name, module in agent.policy_net.named_children():
        if hasattr(module, 'in_features'):
            layers.append((module.in_features, module.out_features))
    
    # Create figure
    fig = plt.figure(figsize=(10, 8))
    
    # Plot layers
    n_layers = len(layers)
    max_neurons = max(max(in_size, out_size) for in_size, out_size in layers)
    
    for i, (in_size, out_size) in enumerate(layers):
        # Plot neurons
        x = i / (n_layers - 1)
        for j in range(max(in_size, out_size)):
            y = j / (max_neurons - 1)
            if j < in_size:
                plt.scatter([x], [y], c='b')
            if j < out_size and i < n_layers - 1:
                plt.scatter([x + 1/(n_layers-1)], [y], c='b')
    
    plt.title('Agent Network Architecture')
    plt.axis('off')
    
    if save_path:
        plt.savefig(save_path)
    
    if show:
        plt.show()
    
    return fig 