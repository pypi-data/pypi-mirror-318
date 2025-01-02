
<p align="center"><img src="/logo.gif" alt="Logo" width="200"></p>

---

# docbuilderpy

[![codecov](https://codecov.io/github/janmarkuslanger/docbuilderpy/graph/badge.svg?token=MFSMU2XYDI)](https://codecov.io/github/janmarkuslanger/docbuilderpy)

**docbuilderpy** is a tool for easily generating documentation for Python projects. It provides default functionality for generating documentation in Markdown format and allows users to include custom generators.

## 🚀 Installation

To install **docbuilderpy**, run the following command:

```bash
pip install docbuilderpy
```

## 📖 Usage

Once installed, you can use the `docbuilderpy` command in the terminal. The basic syntax is:

```bash
docbuilderpy PATH [OPTIONS]
```

### Options

- **`path`** *(required)*: The path to the Python project or directory to analyze.
- **`--output`, `-o`** *(optional)*: The path where the generated documentation will be saved. Default: `docs`.
- **`--format`, `-f`** *(optional)*: The output format of the documentation. Currently supported: `markdown` (default).
- **`--custom_generator`, `-cg`** *(optional)*: Path to a Python file containing a custom generator class.

### Examples

#### Generate standard documentation

Create documentation in Markdown format and save it to the default output path `docs`:

```bash
docbuilderpy ./my_project
```

#### Save documentation to a custom path

Create documentation and save it to a custom directory:

```bash
docbuilderpy ./my_project --output ./custom_docs
```

#### Use a custom generator

Use a custom generator class from the file `custom_generator.py`:

```bash
docbuilderpy ./my_project --custom_generator ./custom_generator.py
```

## 🔧 Creating Custom Generators

If you want to extend the default functionality, you can create your own generator classes. The custom class must inherit from the abstract classes `Generator`, `SingleFileGenerator` or `MultiFileGenerator`.

`Generator` if you want to control the complete generation process.

`SingleFileGenerator` if you want to create a single file doc file.

`MultiFileGenerator` if you want to create a multi file doc file.

### Example: Custom Generator Class

Create a file `custom_generator.py` with the following content:

```python
from docbuilderpy.generate import Generator
from typing import List
from docbuilderpy.definitions import Definition

class CustomGenerator(SingleFileGenerator):
    source_path: str
    output_path: str
    file_format: str
    definitions: List[Union[FunctionDefinition, ClassDefinition]]

    def generate_file(self) -> str:
        # you can access definitions and create your own output
        return "This is a custom generator!"
```

Then, use this class with the `--custom_generator` option:

```bash
docbuilderpy ./my_project --custom_generator ./custom_generator.py
```

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy using **docbuilderpy**! If you have questions or issues, feel free to open an issue on GitHub.
