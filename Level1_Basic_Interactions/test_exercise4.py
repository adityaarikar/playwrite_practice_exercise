"""
Exercise 4 — Search for Different Products
Use parametrization:
Test should effectively do search product -> 	submit -> verify result
"""
import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.parametrize("search_prod, result",[
    ("Iphone 15", "over 50,000 results for"),
    ("Laptops", "over 50,000 results for"),
    ("Mobiles", "over 70,000 results for"),
])
def test_search_different_products(playwright: Playwright, search_prod, result):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open amazon website
    page.goto("https://www.amazon.in/")

    page.get_by_role("searchbox", name="Search Amazon.in").fill(search_prod)
    page.locator("#nav-search-submit-button").click()

    # Verify results found on the page
    expect(page.get_by_text(result)).to_be_visible()
