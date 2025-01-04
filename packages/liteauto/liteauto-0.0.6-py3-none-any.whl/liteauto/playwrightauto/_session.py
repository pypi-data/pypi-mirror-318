from playwright.sync_api import sync_playwright
import json
import os
import time
from loguru import logger


class BrowserSession:
    def __init__(self, cookies_file: str | None = "huggingchat_cookies.json",
                 url: str | None = None,
                 username: str | None = None,
                 password: str | None = None, headless=None):
        self.cookies_file = cookies_file
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.start(url=url, username=username, password=password,headless=headless)

    def start(self, url, username, password, headless=None):
        """Start a browser session with cookie management"""
        logger.debug(f"Starting browser session for {url}")

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True if headless is None else headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        # Try to load existing cookies
        if self._load_cookies():
            logger.debug("Found existing cookies, attempting to use them...")
            try:
                self._try_existing_session(url)
            except Exception as e:
                logger.debug(f"Session expired or invalid: {e}")
                self._login_and_save_cookies(url, username, password)
        else:
            logger.debug("No existing cookies found")
            self._login_and_save_cookies(url, username, password)

    def _load_cookies(self):
        """Load cookies from file if they exist"""
        if os.path.exists(self.cookies_file):
            try:
                with open(self.cookies_file, 'r') as f:
                    cookies = json.load(f)
                logger.debug(f"Loading {len(cookies)} cookies from {self.cookies_file}")
                self.context.add_cookies(cookies)
                return True
            except Exception as e:
                logger.debug(f"Error loading cookies: {e}")
                return False
        return False

    def _save_cookies(self):
        """Save current cookies to file"""
        cookies = self.context.cookies()
        with open(self.cookies_file, 'w') as f:
            json.dump(cookies, f)
        logger.debug(f"Saved {len(cookies)} cookies to {self.cookies_file}")

    def _try_existing_session(self, url):
        """Try to use existing session"""
        logger.debug("Attempting to use existing session...")
        self.page.goto(url)

        # Wait for page load
        self.page.wait_for_load_state('networkidle')

        # Check if we need to login using the specific button class
        sign_in_button = self.page.locator(
            'button.flex.w-full.flex-wrap.items-center.justify-center.whitespace-nowrap.rounded-full')
        if sign_in_button.is_visible():
            raise Exception("Session expired - need to login again")

        logger.debug("Existing session valid!")

    def _login_and_save_cookies(self, url, username, password):
        """Perform login and save new cookies"""
        logger.debug("Performing fresh login...")
        self.page.goto(url)

        # Wait for the specific sign in button using its exact class
        logger.debug("Waiting for sign in button...")
        self.page.wait_for_selector(
            'button.flex.w-full.flex-wrap.items-center.justify-center.whitespace-nowrap.rounded-full')

        # Click the sign in button
        logger.debug("Clicking sign in button...")
        self.page.click('button.flex.w-full.flex-wrap.items-center.justify-center.whitespace-nowrap.rounded-full')

        # Wait for redirect and form
        logger.debug("Waiting for login form...")
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_selector('input[name="username"]', timeout=10000)

        # Fill in credentials
        logger.debug("Filling credentials...")
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)

        # Submit the form
        logger.debug("Submitting login form...")
        self.page.click('button[type="submit"]')

        # Wait for login to complete
        logger.debug("Waiting for login to complete...")
        self.page.wait_for_load_state('networkidle')
        time.sleep(5)  # Additional wait to ensure completion

        # Save the new cookies
        self._save_cookies()
        logger.debug("Login successful, new cookies saved")

    def close(self):
        """Clean up resources"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        logger.debug("Browser session closed")


class HFBrowerSession(BrowserSession):
    def __init__(self, cookies_file="huggingchat_cookies.json",
                 url="https://huggingface.co/chat/",
                 username="santhoshkammari1999@gmail.com",
                 password="SK99@pass123",
                 headless=True):
        super().__init__(cookies_file, url, username, password,headless=headless)
