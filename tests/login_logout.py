from pytest_bdd import scenario, given, when, then


@scenario('features/login_logout.feature', 'Successful login and logout')
def test_login_logout():
    pass


@given('I am on the login page')
async def open_login_page(page):
    # page = browser.new_page()
    await page.goto('https://www.roundcube.sk/')
    return page


@when('I enter my username and password')
async def enter_credentials(page):
    await page.fill('input[id="rcmloginuser"]', 'babulic@septimus.sk')
    await page.fill('input[id="rcmloginpwd"]', 'Mrk3')


@when('I click on the login button')
async def click_login(page):
    await page.click('id=rcmloginsubmit')


@then('I should be redirected to the inbox page')
async def verify_inbox(page):
    # Optionally wait for navigation to ensure the URL has changed
    await page.wait_for_url('https://www.roundcube.sk/?_task=mail&_mbox=INBOX')
    assert page.url == 'https://www.roundcube.sk/?_task=mail&_mbox=INBOX'


@when('I click on the logout button')
async def click_logout(page):
    await page.click('text=Logout')


@then('I should be redirected to the login page')
async def verify_login_page(page):
    # Optionally wait for navigation to ensure the URL has changed
    await page.wait_for_url('https://www.roundcube.sk/?_task=logout')
    assert page.url == 'https://www.roundcube.sk/?_task=logout'