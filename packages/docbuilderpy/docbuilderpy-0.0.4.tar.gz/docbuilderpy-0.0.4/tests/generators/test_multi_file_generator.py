from docbuilderpy.generators.multi_file_generator import MultiFileGenerator

# from tests.utility import setup_test_environment


def setup_test_environment(tmp_path):
    my_lib_folder = tmp_path / "my_lib"
    my_lib_folder.mkdir()

    test_class_file = my_lib_folder / "test_class.py"
    test_class_content = """
class TestClass:
    def my_method(self):
        return "Hello from my_method"
"""
    test_class_file.write_text(test_class_content)

    utility_folder = my_lib_folder / "utility"
    utility_folder.mkdir()

    is_test_file = utility_folder / "is_test.py"
    is_test_content = """
def is_test():
    return True

def is_another_test():
    return True
"""
    is_test_file.write_text(is_test_content)

    return my_lib_folder


class TestGenerator(MultiFileGenerator):
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

    base_path = tmp_path / "my_output" / "my_lib"

    assert (base_path / "test_class.html").exists()
    assert (base_path / "utility/is_test.html").exists()
