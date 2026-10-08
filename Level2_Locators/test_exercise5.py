"""
Exercise 5 — Identify Product Results
Search Product
Verify details like Product title, product price, product rating, Number of views
"""
import time
from playwright.sync_api import Playwright, expect


def test_identify_product(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to amazon
    page.goto("https://www.amazon.in/")

    # Search the product on searchbar
    page.locator("#twotabsearchtextbox.nav-input.nav-progressive-attribute").fill("Iphone 16")
    page.locator("#nav-search-submit-button").click()

    # Validate the result is visible
    expect(page.get_by_text('over 50,000 results for "Iphone 16"')).to_be_visible()

    # get the products that has iphone16 in there title
    products = page.locator(".puisg-row").filter(has_text="iPhone 16 128 GB").first

    # Product title, product price, product rating, Number of views
    prod_title = products.locator(".s-title-instructions-style").inner_text()
    print(f"Product title :- {prod_title}")

    prod_price = products.locator(".a-price-whole").inner_text()
    print(f"Product price :- {prod_price}")

    prod_rating = products.locator(".mvt-review-star-with-margin").inner_text()
    print(f"Product rating :- {prod_rating}")