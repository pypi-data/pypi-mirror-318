from enum import Enum
from typing import Dict

from pydantic import BaseModel


class Solver(str, Enum):
    NAIVE = "naive"
    OLYMPIC = "olympic"
    SNA = "sna"
    GPT = "gpt"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    @property
    def pass_probability(self) -> float:
        return DIFFICULTY_TO_PASS_PROBABILITY[self]


class APIModelIdentifier(BaseModel):
    language: str
    model_name: str
    is_stemmed: bool = False


DIFFICULTY_TO_PASS_PROBABILITY: Dict[Difficulty, float] = {
    Difficulty.EASY: 0.4,
    Difficulty.MEDIUM: 0.2,
    Difficulty.HARD: 0,
}
