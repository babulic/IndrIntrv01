from pytest_bdd import scenario, given, when, then
from playwright.sync_api import sync_playwright

@scenario('../features/login_logout.feature', 'Successful login and logout')
def test_login_logout():
    """
    Scenario: Successful login and logout
    """
    pass


@given('I am on the login page')
def open_login_page(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.roundcube.sk/')
    return page


@when('I enter my username and password')
def enter_credentials(page):
    page.fill('input[id="rcmloginuser"]', 'babulic@septimus.sk')  # //input[@id='rcmloginuser']
    page.fill('input[id="rcmloginpwd"]', 'Mrk3')  # //input[@id='rcmloginpwd']


@when('I click on the login button')
def click_login(page):
    page.click('id=rcmloginsubmit')  # //button[@id='rcmloginsubmit']


@then('I should be redirected to the inbox page')
def verify_inbox(page):
    assert page.url == 'https://www.roundcube.sk/?_task=mail&_mbox=INBOX'


@when('I click on the logout button')
def click_logout(page):
    page.click('text=Logout')  # //span[contains(text(),'Logout')]


@then('I should be redirected to the login page')
def verify_login_page(page):
    assert page.url == 'https://www.roundcube.sk/?_task=logout'
