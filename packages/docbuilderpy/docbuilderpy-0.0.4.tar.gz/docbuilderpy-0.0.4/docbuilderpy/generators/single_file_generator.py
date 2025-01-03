import abc
import os
from typing import List, Union, override
from docbuilderpy.generators.generator import Generator
from docbuilderpy.load_file import load_file
from docbuilderpy.analyze_definitions import analyze_definitions
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class SingleFileGenerator(Generator, abc.ABC):
    source_path: str
    output_path: str
    file_format: str
    definitions: List[Union[FunctionDefinition, ClassDefinition]]

    @override
    def generate(self) -> None:
        self.definitions = []
        for root, _, files in os.walk(self.source_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    code = load_file(file_path)
                    self.definitions.extend(analyze_definitions(code, file_path))

        content = self.generate_file()
        output_file_path = self.output_path + "." + self.file_format
        with open(output_file_path, "w") as output_file:
            output_file.write(content)

    @override
    @abc.abstractmethod
    def generate_file(self) -> str:
        pass
