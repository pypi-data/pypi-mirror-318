from typing import List, Optional, Union

from codenames.classic.state import ClassicOperativeState, ClassicSpymasterState
from codenames.duet.state import DuetOperativeState, DuetSpymasterState
from pydantic import BaseModel, model_validator

from .base import APIModelIdentifier, Solver


class LoadModelsRequest(BaseModel):
    model_identifiers: List[APIModelIdentifier] = []
    load_default_models: bool = True


class BaseGenerateRequest(BaseModel):
    solver: Solver = Solver.NAIVE
    model_identifier: Optional[APIModelIdentifier]


class GenerateClueRequest(BaseGenerateRequest):
    spymaster_state: Union[ClassicSpymasterState, DuetSpymasterState]


class GenerateGuessRequest(BaseGenerateRequest):
    operative_state: Union[ClassicOperativeState, DuetOperativeState]


class StemRequest(BaseModel):
    word: str
    model_identifier: APIModelIdentifier


class MostSimilarRequest(BaseModel):
    word: Optional[str]
    vector: Optional[List[float]]
    model_identifier: APIModelIdentifier
    top_n: int = 10

    @model_validator(mode="before")
    @classmethod
    def check_word_xor_vector(cls, values):  # pylint: disable=no-self-argument
        word = values.get("word")
        vector = values.get("vector")
        if word and vector:
            raise ValueError("Exactly one of word or vector must be provided (both were provided).")
        if not word and not vector:
            raise ValueError("Exactly one of word or vector must be provided (neither were provided).")
        return values


class SimpleClueRequest(BaseModel):
    positive: List[str]
    negative: List[str] = []
    top_n: int = 10
    language: Optional[str]
    model_identifier: Optional[APIModelIdentifier]

    @model_validator(mode="before")
    @classmethod
    def check_language_xor_model(cls, values):
        language = values.get("language")
        model_identifier = values.get("model_identifier")
        if language and model_identifier:
            raise ValueError("Exactly one of language or model_identifier must be provided (both were provided).")
        if not language and not model_identifier:
            raise ValueError("Exactly one of language or model_identifier must be provided (neither were provided).")
        return values
