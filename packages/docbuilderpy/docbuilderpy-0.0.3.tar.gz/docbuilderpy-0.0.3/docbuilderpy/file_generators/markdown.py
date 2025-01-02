from typing import List, Union
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition
from docbuilderpy.generators.multi_file_generator import MultiFileGenerator


class Markdown(MultiFileGenerator):
    source_path: str
    output_path: str
    file_format: str = "md"
    definitions: List[Union[FunctionDefinition, ClassDefinition]]

    def generate_file(self) -> str:
        content = "# Documentation"
        for item in self.definitions:

            if isinstance(item, FunctionDefinition):
                content += f"\n\n## Function: `{item.name}`\n"
                content += f"- File: {item.file}\n"

                if item.arguments:
                    content += f"- Args: {', '.join(item.arguments)}\n"

            elif isinstance(item, ClassDefinition):
                content += f"\n\n## Class: `{item.name}`\n"
                content += f"- File: {item.file}\n"

                if item.methods:
                    for method in item.methods:
                        content += f"\n\n### Method: `{method.name}`\n"

                        if method.arguments:
                            content += f"- Args: {', '.join(method.arguments)}\n"

            if item.docstring:
                content += f"- Description: {item.docstring}"

        return content

    def get_file_format(self) -> str:
        return "md"
