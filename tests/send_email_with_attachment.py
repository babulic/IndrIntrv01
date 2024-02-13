from pytest_bdd import scenario, given, when, then

@when('I attach a file')
def attach_file(page):
    # Assuming there's an input for file uploads with the ID 'file-upload'
    page.set_input_files('input#file-upload', '/path/to/your/file.txt')
