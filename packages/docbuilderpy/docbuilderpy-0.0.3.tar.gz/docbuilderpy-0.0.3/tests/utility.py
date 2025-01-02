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
