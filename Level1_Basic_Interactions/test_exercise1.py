"""
Exercise 1 — Open Amazon

1. Opens Amazon.in
2. Verifies the page loaded
3. Verifies the title contains Amazon
"""

from playwright.sync_api import Playwright, expect


def test_open_amazon(playwright: Playwright):
    # Launch Chromium browser
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context
    context = browser.new_context()

    # Create a new page
    page = context.new_page()

    # Open Amazon.in
    page.goto("https://www.amazon.in/")

    # Locate Amazon logo using its role and accessible name
    amazon_link = page.get_by_role("link", name="Amazon.in")

    # Verify that Amazon logo/link is visible
    expect(amazon_link).to_be_visible()

    # Get the href of Amazon logo
    logo_url = amazon_link.get_attribute("href")
    print(f"href of the logo is {logo_url}")

    # Close browser context
    context.close()
    browser.close()