from typing import List, Optional

from codenames.generic.move import Clue, Guess
from pydantic import BaseModel

from .base import APIModelIdentifier, Solver


class BaseResponse(BaseModel):
    pass


class LoadModelsResponse(BaseResponse):
    success_count: int
    fail_count: int


class GenerateClueResponse(BaseResponse):
    suggested_clue: Clue
    used_solver: Solver
    used_model_identifier: Optional[APIModelIdentifier]


class GenerateGuessResponse(BaseResponse):
    suggested_guess: Guess
    used_solver: Solver
    used_model_identifier: Optional[APIModelIdentifier]


class StemResponse(BaseResponse):
    root: str


class Similarity(BaseModel):
    word: str
    similarity: float

    def __hash__(self):
        return hash((self.word, self.similarity))


class MostSimilarResponse(BaseResponse):
    most_similar: List[Similarity]


class SimpleClueResponse(BaseModel):
    suggested_clues: List[str]
    used_model_identifier: APIModelIdentifier
