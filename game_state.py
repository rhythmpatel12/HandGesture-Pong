from enum import Enum, auto

class GameState(Enum):
    START_SCREEN = auto()
    PLAYING_GAME = auto()
    END_SCREEN = auto()