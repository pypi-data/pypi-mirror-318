import abc
import os
from typing import List, Union, override
from docbuilderpy.generators.generator import Generator
from docbuilderpy.load_file import load_file
from docbuilderpy.analyze_definitions import analyze_definitions
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class MultiFileGenerator(Generator, abc.ABC):
    source_path: str
    output_path: str
    file_format: str
    definitions: List[Union[FunctionDefinition, ClassDefinition]] = []

    @override
    def generate(self) -> None:
        for root, _, files in os.walk(self.source_path):
            for file in files:
                if file.endswith(".py") and not file.endswith("__init__.py"):
                    file_path = os.path.join(root, file)
                    code = load_file(file_path)
                    self.definitions = analyze_definitions(code, file_path)

                    relative_path = os.path.relpath(file_path, self.source_path)
                    output_file_path = os.path.join(self.output_path, relative_path)

                    output_dir = os.path.dirname(output_file_path)
                    os.makedirs(output_dir, exist_ok=True)

                    content = self.generate_file()

                    with open(
                        output_file_path + "." + self.file_format, "w"
                    ) as output_file:
                        output_file.write(content)

    @override
    @abc.abstractmethod
    def generate_file(self) -> str:
        pass
