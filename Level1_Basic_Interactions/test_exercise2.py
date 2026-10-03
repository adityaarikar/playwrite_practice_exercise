"""
Exercise 2 — Locate Search Box
1. Find the Amazon search box.
2. Try three different locators to locate it.
"""
from playwright.sync_api import Playwright, expect


def test_locate_search_box(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to amazon.in website
    page.goto("https://www.amazon.in/")

    # Find the searchbox.
    searchbox1 = page.get_by_role("searchbox")
    expect(searchbox1).to_be_visible()

    searchbox2 = page.get_by_placeholder("Search Amazon.in")
    expect(searchbox2).to_be_visible()

    searchbox3 = page.locator("#twotabsearchtextbox")
    expect(searchbox3).to_be_visible()

    context.close()
    browser.close()
