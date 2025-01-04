from playwright.sync_api import sync_playwright
import json
import os
import time
from datetime import datetime


class BrowserSession:
    def __init__(self, cookies_file="browser_cookies.json"):
        self.cookies_file = cookies_file
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self, url, username, password):
        """Start a browser session with cookie management"""
        print(f"Starting browser session for {url}")

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        # Try to load existing cookies
        if self._load_cookies():
            print("Found existing cookies, attempting to use them...")
            try:
                self._try_existing_session(url)
            except Exception as e:
                print(f"Session expired or invalid: {e}")
                self._login_and_save_cookies(url, username, password)
        else:
            print("No existing cookies found")
            self._login_and_save_cookies(url, username, password)

    def _load_cookies(self):
        """Load cookies from file if they exist"""
        if os.path.exists(self.cookies_file):
            try:
                with open(self.cookies_file, 'r') as f:
                    cookies = json.load(f)
                print(f"Loading {len(cookies)} cookies from {self.cookies_file}")
                self.context.add_cookies(cookies)
                return True
            except Exception as e:
                print(f"Error loading cookies: {e}")
                return False
        return False

    def _save_cookies(self):
        """Save current cookies to file"""
        cookies = self.context.cookies()
        with open(self.cookies_file, 'w') as f:
            json.dump(cookies, f)
        print(f"Saved {len(cookies)} cookies to {self.cookies_file}")

    def _try_existing_session(self, url):
        """Try to use existing session"""
        print("Attempting to use existing session...")
        self.page.goto(url)

        # Wait a bit and check if we're still logged in
        # You'll need to customize this check based on your website
        self.page.wait_for_load_state('networkidle')

        # If we detect login page or other indicators of session expiry,
        # raise an exception
        if "login" in self.page.url.lower():
            raise Exception("Redirected to login page - session expired")

        print("Existing session valid!")

    def _login_and_save_cookies(self, url, username, password):
        """Perform login and save new cookies"""
        print("Performing fresh login...")
        self.page.goto(url)

        # You'll need to customize these selectors based on your website
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')

        # Wait for login to complete
        self.page.wait_for_load_state('networkidle')

        # Save the new cookies
        self._save_cookies()
        print("Login successful, new cookies saved")

    def close(self):
        """Clean up resources"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("Browser session closed")

if __name__ == '__main__':
    # Create a new session
    session = BrowserSession()

    # Start the session with your website
    session.start(
        url="https://huggingface.co/chat/",
        username="santhoshkammari1999@gmail.com",
        password="SK99@pass123"
    )

    # Do your work here...

    # Close when done
    session.close()