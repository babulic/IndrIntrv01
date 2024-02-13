from pytest_bdd import scenario, given, when, then


@scenario('../features/send_email_with_attachment.feature', 'Send an email with attachment')
def test_send_email_with_attachment():
    """
    Scenario: Send an email with attachment
    """
    pass


@when('I attach a file')
def attach_file(page):
    # Assuming there's an input for file uploads with the ID 'file-upload'
    page.set_input_files('input#file-upload', '/path/to/your/file.txt')
