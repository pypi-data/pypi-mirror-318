from typing import List, Union
from docbuilderpy.generators.generator import Generator
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class TestGenerator(Generator):
    def generate(self, source_path: str, output_path: str) -> None:
        pass

    def generate_file(
        self, definitions: List[Union[FunctionDefinition, ClassDefinition]]
    ) -> str:
        return "test"

    def get_file_format(self) -> str:
        return "test_format"


def test_generate():
    generator = TestGenerator()
    assert generator.generate("source_path", "output_path") is None


def test_generate_file():
    generator = TestGenerator()
    definitions = []
    result = generator.generate_file(definitions)
    assert result == "test"


def test_get_file_format():
    generator = TestGenerator()
    result = generator.get_file_format()
    assert result == "test_format"
