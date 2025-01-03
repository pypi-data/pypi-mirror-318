import abc
from typing import List, Union
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class Generator(abc.ABC):
    source_path: str
    output_path: str
    file_format: str
    definitions: List[Union[FunctionDefinition, ClassDefinition]]

    @abc.abstractmethod
    def generate(self) -> None:
        pass

    @abc.abstractmethod
    def generate_file(self) -> str:
        pass
