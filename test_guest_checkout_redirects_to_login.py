"""
Test case: Guest checkout redirects to login page

This end-to-end test verifies that a guest (unauthenticated) user is redirected to the login page
when attempting to proceed to checkout on the whey-protein.ch e-commerce website.

Test steps:
1. Open the home page.
2. Search for the term "creatin".
3. Confirm that search results are displayed.
4. Click on a specific product ("Creatin Monohydrat") from the list.
5. Verify the product detail page has loaded.
6. Add the product to the cart.
7. Click the checkout button.
8. Assert the user is redirected to the login page.

Tech stack:
- Python
- Selenium (Firefox with geckodriver)
- WebDriverWait + Expected Conditions (EC)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_checkout_redirects_to_login():
    # Setup: configure Firefox driver (Termux-compatible path)
    service = Service(executable_path="/data/data/com.termux/files/usr/bin/geckodriver")
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service)

    wait = WebDriverWait(driver, 10)

    # Step 1: Open the home page
    driver.get("https://whey-protein.ch/")
    assert "Lee-Sport" in driver.title, "Home page did not load correctly"

    # Step 2: Search for "creatin"
    search_input = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_input.send_keys("creatin")
    search_input.submit()

    # Step 3: Verify search results are present
    results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-media-image")))
    assert len(results) > 0, "No search results found for 'creatin'"

    # Step 4: Click on the specific product "Creatin Monohydrat"
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[@class="js-product-link" and normalize-space()="Creatin Monohydrat"]')
        )
    ).click()

    # Step 5: Verify the product detail page is loaded
    assert "Creatin" in driver.title, "Product detail page did not load"

    # Step 6: Click the "Add to Cart" button
    add_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[span[text()="In den Warenkorb legen"]]'))
    )
    assert add_btn.is_displayed(), "'Add to Cart' button not visible"
    add_btn.click()

    # Step 7: Click the "Checkout" button
    checkout_btn = wait.until(EC.element_to_be_clickable((By.NAME, "checkout")))
    assert checkout_btn.is_displayed(), "'Checkout' button not visible"
    checkout_btn.click()

    # Step 8: Assert the user is redirected to the login page
    wait.until(EC.title_contains("Konto"))
    assert "Konto" in driver.title, "User was not redirected to login page"

    # Cleanup: Close the browser
    driver.quit()
