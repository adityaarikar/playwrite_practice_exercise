"""
Exercise 3 — Search for iPhone 15
1. Amazon -> Search "iPhone 15" -> Submit search -> Verify search results are displayed
"""

from playwright.sync_api import Playwright, expect


def test_search_iphone(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to amazon.in
    page.goto("https://www.amazon.in/")

    # Get the searchbox
    page.get_by_role("searchbox", name="Search Amazon.in").fill("Iphone 15")
    page.locator("#nav-search-submit-button").click()

    # Verify results found on the page
    expect(page.get_by_text("over 50,000 results for")).to_be_visible()