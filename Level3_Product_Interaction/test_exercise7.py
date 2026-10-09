"""
Exercise 7 — Open a Product
Search Product
Find the product
Click and go to details page
Verify details like Product title, product price, product rating, Number of views
"""
import time
from playwright.sync_api import Playwright, expect


def test_open_product(broweseInstance):
    page = broweseInstance

    # Go to amazon
    page.goto("https://www.amazon.in/")

    # Search the product on searchbar
    page.locator("#twotabsearchtextbox.nav-input.nav-progressive-attribute").fill("Iphone 16")
    page.locator("#nav-search-submit-button").click()

    # Validate the result is visible
    expect(page.get_by_text('over 50,000 results for "Iphone 16"')).to_be_visible()

    # get the products that has iphone16 in there title
    product = page.locator(".puisg-row").filter(has_text="iPhone 16 128 GB").first

    expect(product).to_be_visible()

    product_link = product.locator(".s-title-instructions-style").get_by_role('link')

    with page.context.expect_page() as product_page:
        product_link.click()

    product_page = product_page.value

    product_title = product_page.locator("#productTitle")
    expect(product_title).to_be_visible()
    assert "Apple iPhone 16 128 GB" in product_title.inner_text()
    print(f"Product Title :- {product_title.inner_text()}")

    product_price = product_page.locator(".priceToPay")
    expect(product_price).to_be_visible()
    assert "76,999" in product_price.inner_text()
    print(f"Product Price :- {product_price.inner_text()}")

    product_review = product_page.get_by_role("link", name="2,757 Reviews")
    expect(product_review).to_be_visible()
    assert "2,757" in product_review.inner_text()
    print(f"Product Reviews :- {product_review.inner_text()}")

    time.sleep(10)
