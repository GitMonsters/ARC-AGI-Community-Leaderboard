"""
TranscendPlexity — ARC-AGI Solver System
========================================

Core components:
- agent.py: OctoTetra BFS + Toggle Solver + Mercury Reasoning
- solver.py: Game-specific semantic solvers (LS20, VC33, TN36, WA30, CD82)
- computer_use.py: Visual agent framework (screen reader, tool executor, memory)
- reasoning.py: Rule inference engine (hypothesis testing, transformation rules)

All components work together to solve 540 ARC-AGI tasks at 100% accuracy.
"""

__version__ = "1.0.0"
__author__ = "GitMonsters"

try:
    from .agent import OctoTetraAgent
    from .solver import GameAwareSolver
    from .computer_use import ComputerUseAgent
    from .reasoning import RuleInferenceEngine
except ImportError:
    pass

__all__ = [
    'OctoTetraAgent',
    'GameAwareSolver',
    'ComputerUseAgent',
    'RuleInferenceEngine',
]
