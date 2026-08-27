#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Verify that home page is visible successfully
#4. Add products to cart
#5. Click 'Cart' button
#6. Verify that cart page is displayed
#7. Click 'X' button corresponding to particular product
#8. Verify that product is removed from the cart

from QAStudy.Checkout_functions import add_product_to_cart
from playwright.sync_api import sync_playwright, expect

def test_remove_prodcuts_from_cart():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        expect(page).to_have_title("Automation Exercise")

        product_id = add_product_to_cart(page, product_index=3)

        page.locator("#header").get_by_role("link", name="Cart").click()

        expect(page).to_have_title("Automation Exercise - Checkout")

        page.locator(f'a.cart_quantity_delete[data-product-id="{product_id}"]').click()

        expect(page.get_by_text("Cart is empty!")).to_be_visible()

        browser.close()