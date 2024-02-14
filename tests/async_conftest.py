# async_conftest.py
import pytest
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        # Launch a browser instance
        browser = await p.chromium.launch()
        yield browser
        # Ensure the browser is closed when the tests are done
        await browser.close()


@pytest.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        yield page
        await browser.close()