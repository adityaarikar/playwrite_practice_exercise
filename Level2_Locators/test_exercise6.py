"""
Exercise 6 — Count Search Results
Search for product laptop
Find the product-result elements. Then determine how many products are displayed.
Use Playwright's locator count functionality.
Your test should assert something like -> number of products > 0
"""

from playwright.sync_api import Playwright, expect


def test_count_products(broweseInstance):
    page = broweseInstance
    # Go to amazon
    page.goto("https://www.amazon.in/")

    # Search the product on searchbar
    page.locator("#twotabsearchtextbox.nav-input.nav-progressive-attribute").fill("Iphone 16")
    page.locator("#nav-search-submit-button").click()

    # Validate the result is visible
    expect(page.get_by_text('over 50,000 results for "Iphone 16"')).to_be_visible()

    # get the products that has iphone16 in there title
    products = page.locator(".puisg-row").filter(has_text="iPhone 16 128 GB")

    expect(products.first).to_be_visible()

    print(f"Number of products :- {products.count()}")