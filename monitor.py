from playwright.sync_api import sync_playwright, TimeoutError
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_url_content(url, target_text):
    """
    Visits a URL using Playwright and checks if target_text is present on the page.
    Returns (success_boolean, message_string)
    """
    try:
        with sync_playwright() as p:
            # Launch a headless chromium browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Set a timeout of 30 seconds for navigation
            page.goto(url, timeout=30000)
            
            # Wait for the network to be idle to ensure dynamic content loads
            try:
                page.wait_for_load_state('networkidle', timeout=10000)
            except TimeoutError:
                logging.warning("Network did not idle in time, proceeding anyway...")
                
            # Get all the visible text on the page
            page_text = page.locator("body").inner_text()
            
            if target_text.lower() in page_text.lower():
                browser.close()
                return True, "Target text found on the page."
            else:
                browser.close()
                return False, "Target text was NOT found on the page."
                
    except TimeoutError:
        return False, "Timeout: Page took too long to load."
    except Exception as e:
        return False, f"Error: {str(e)}"

# For local testing if run directly
if __name__ == "__main__":
    test_url = "https://example.com"
    test_text = "Example Domain"
    success, msg = check_url_content(test_url, test_text)
    print(f"Result: {success} - {msg}")
