"""
Test case: Guest checkout redirects to login page

This end-to-end test verifies that an unauthenticated (guest) user is redirected to the login page
when attempting to proceed to checkout on the whey-protein.ch website.

Test flow:
1. Open the main store page.
2. Search for the term "creatin".
3. Ensure that search results are returned.
4. Click on the "Creatin Monohydrat" product from the list.
5. Verify that the product detail page has loaded.
6. Click the "In den Warenkorb legen" (Add to Cart) button.
7. Click the "Zur Kasse gehen" (Checkout) button.
8. Assert that the user is redirected to the login page.

Technology stack:
- Python
- Selenium WebDriver (Firefox, via geckodriver)
- Pytest-compatible function
- Explicit waits via WebDriverWait and expected_conditions (EC)



Author: jezierski999@gmail.com
"""

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
