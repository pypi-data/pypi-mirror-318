import abc
from typing import List
from dataclasses import dataclass


@dataclass
class Definition(abc.ABC):
    type: str
    name: str
    docstring: str | None


@dataclass
class FunctionDefinition(Definition):
    type = "function"
    file: str
    arguments: list[str] | None = None


@dataclass
class MethodDefinition(Definition):
    arguments: list[str]


@dataclass
class ClassDefinition(Definition):
    type = "class"
    file: str
    methods: List[MethodDefinition] | None = None
