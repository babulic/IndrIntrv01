from pytest_bdd import scenario, given, when, then

@when('I click on the compose button')
def click_compose(page):
    page.click('text=Compose')

@when('I fill in the recipient with my email from contacts')
def fill_recipient(page):
    page.fill('input[name="to"]', 'your_email@example.com')

@when('I fill in the subject and body of the email')
def fill_subject_and_body(page):
    page.fill('input[name="subject"]', 'Test Subject')
    page.fill('textarea[name="body"]', 'This is a test email.')

@when('I click on the send button')
def click_send(page):
    page.click('text=Send')

@then('the email should be sent successfully')
def verify_email_sent(page):
    # Assuming there's a notification or you are redirected to "Sent" folder
    assert page.text_content('.notification') == 'Email sent successfully'
