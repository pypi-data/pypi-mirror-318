"""Core module for the game engine. Contains the main classes and utilities."""

from .game import Game
from .scene import Scene
from .scene_manager import SceneManager
from .input_manager import InputManager
from .entity import Entity
from .asset_manager import AssetManager
from .settings import Settings
from .game_context import create_game_context, GameContext
from . import dataclasses
from . import wrappers
from . import utils

__all__ = [
    'Game',
    'Scene',
    'SceneManager',
    'InputManager',
    'Entity',
    'AssetManager',
    'Settings',
    'GameContext',
    'create_game_context',
    'dataclasses',
    'wrappers',
    'utils',
]
