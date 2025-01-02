from docbuilderpy.file_generators.markdown import Markdown
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


def test_markdown_generator():
    definitions = [
        FunctionDefinition(
            type="function",
            name="my_function",
            docstring="This is a function.",
            file="file.py",
        ),
        ClassDefinition(
            type="class", name="MyClass", docstring="This is a class.", file="file.py"
        ),
    ]

    markdown_generator = Markdown()
    markdown_generator.definitions = definitions
    output = markdown_generator.generate_file()

    assert "# Documentation" in output
    assert "## Function: `my_function`" in output
    assert "This is a function." in output
    assert "## Class: `MyClass`" in output
    assert "This is a class." in output
