import pytest
from playwright.sync_api import expect

# Define a simple test class. Pytest will discover tests starting with 'test_'.
class TestSearchFunctionality:

    @pytest.mark.parametrize("search_term", ["Playwright automation", "Python pytest"])
    def test_basic_search(self, page, search_term):
        """
        Tests the search functionality on a mock website.
        
        Args:
            page: The Playwright page object provided by the fixture.
            search_term: The term to search for (from parametrize).
        """
        
        print(f"\n--- Running test with search term: '{search_term}' ---")

        # 1. Navigate to the base URL
        page.goto("https://playwright.dev/")
        expect(page).to_have_title("Fast and reliable end-to-end testing | Playwright")
        
        # 2. Find and click the search button/icon
        # Using role and name for robustness
        search_button = page.get_by_role("button", name="Search")
        search_button.click()
        
        # 3. Type the search term into the search input field
        search_input = page.get_by_placeholder("Search docs")
        search_input.fill(search_term)
        
        # 4. Assert that the input field contains the text we just typed
        expect(search_input).to_have_value(search_term)
        
        # 5. Wait for and assert that results are visible
        # We look for a specific heading that indicates search results are loaded
        results_heading = page.locator("nav#doc-search-results h3").first
        expect(results_heading).to_be_visible()
        expect(results_heading).to_contain_text("Results")
        
        # 6. Click the first result link
        first_result_link = page.locator("#doc-search-results a").first
        first_result_link_text = first_result_link.text_content()
        first_result_link.click()

        # 7. Final assertion: Verify we landed on a new page related to the search
        expect(page).to_have_url(lambda url: search_term.lower().replace(" ", "-") in url.lower())
        print(f"Successfully navigated to: {page.url}")
