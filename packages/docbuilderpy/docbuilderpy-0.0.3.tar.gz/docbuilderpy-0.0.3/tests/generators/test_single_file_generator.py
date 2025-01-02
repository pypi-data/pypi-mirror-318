from docbuilderpy.generators.single_file_generator import SingleFileGenerator
from tests.utility import setup_test_environment


class TestGenerator(SingleFileGenerator):
    def generate_file(self):
        return "my_output"

    def get_file_format(self):
        return "html"


def test_generate(tmp_path):
    setup_test_environment(tmp_path)
    tmp_path_str = str(tmp_path)

    generator = TestGenerator()
    generator.source_path = str(tmp_path)
    generator.file_format = "html"
    generator.output_path = tmp_path_str + "/my_output"

    generator.generate()
    output_file = tmp_path / "my_output.html"
    assert output_file.read_text() == "my_output"
