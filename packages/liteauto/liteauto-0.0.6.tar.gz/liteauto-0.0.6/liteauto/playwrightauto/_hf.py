import time
from typing import List, Optional
from datetime import datetime

from loguru import logger


class HuggingFaceAutomation:
    def __init__(self, browser_session):
        """
        Initialize automation with an existing browser session
        """
        self.session = browser_session
        self.page = browser_session.page

    def generate(self, query: str, web_search: bool = False, max_wait_time: int = 300) -> str:
        return self._stream_single_query(
            query=query,
            web_search=web_search,
            max_wait_time=max_wait_time
        )

    def complete(self, query: str, web_search: bool = False, max_wait_time: int = 300) -> str:
        result = [_ for _ in self._stream_single_query(
            query=query,
            web_search=web_search,
            max_wait_time=max_wait_time
        )]
        return "".join(result)

    def _stream_single_query(self, query: str, web_search: bool = False, max_wait_time: int = 300) -> str:
        """
        Process a single query and return the response
        """
        logger.debug(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing query: {query[:50]}...")

        # Clear any existing chat if present
        self._handle_click_new_chat_button()

        # Toggle web search if needed
        self._handle_web_search_toggle(web_search)

        # Type and submit query
        self._handle_enter_query_in_text_area(query=query)

        # Monitor response generation
        logger.debug("Monitoring response generation...")

        start_time = time.time()
        min_chat_start_time = 1
        chat_stream_wait_time = 1
        each_chunk_stream_delay=0.5

        min_chat_start_time += 7 if web_search else 0  # add websearch time

        return self._handle_text_streaming(min_chat_start_time=min_chat_start_time,
                                           start_time=start_time,
                                           max_wait_time=max_wait_time,
                                           chat_stream_wait_time=chat_stream_wait_time,
                                           web_search=web_search,
                                           each_chunk_stream_delay=each_chunk_stream_delay)

    def batch(self,
              queries: List[str],
              web_search: bool = False,
              each_chat_waiting_time: int = 1,
              batch_size: int = 4,
              batch_waiting_time: int = 10) -> List[dict]:
        """
        Process multiple queries with batch processing and waiting times
        """
        results = []

        logger.debug(
            f"\n[{datetime.now().strftime('%H:%M:%S')}] Starting batch processing of {len(queries)} queries...")
        logger.debug(f"Batch size: {batch_size}, Batch wait time: {batch_waiting_time}s")

        for i, query in enumerate(queries, 1):
            logger.debug(f"\n--- Query {i}/{len(queries)} ---")

            # Process the query
            response = self.complete(query=query, web_search=web_search)

            # Store result
            results.append({
                'query': query,
                'response': response,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            # Handle waiting times
            if i < len(queries):  # Don't wait after the last query
                if i % batch_size == 0:
                    logger.debug(f"Completed batch of {batch_size}. Waiting {batch_waiting_time} seconds...")
                    time.sleep(batch_waiting_time)
                else:
                    logger.debug(f"Waiting {each_chat_waiting_time} seconds before next query...")
                    time.sleep(each_chat_waiting_time)

        logger.debug(f"\n[{datetime.now().strftime('%H:%M:%S')}] Completed processing all queries!")
        return results

    def _handle_web_search_toggle(self, web_search):
        if not web_search:
            logger.debug("No web search Toggled")
            return
        logger.debug("Enabling web search...")
        try:
            search_button = self.page.locator('button.base-tool.svelte-10z3gx0').first
            if search_button.is_visible():
                logger.debug("Found search button with class")
                search_button.click()
                logger.debug("Clicked search button")
                time.sleep(1)
            else:
                # Fallback to parent div containing search elements
                search_area = self.page.locator('div.group/tooltip.inline-block.md:relative').first
                if search_area.is_visible():
                    logger.debug("Found search area")
                    search_area.click()
                    logger.debug("Clicked search area")
                    time.sleep(1)
                else:
                    logger.debug("Neither search button nor area found")
                    # Print all buttons for debugging
                    buttons = self.page.locator('button').all()
                    logger.debug(f"Found {len(buttons)} buttons on page")
                    for i, button in enumerate(buttons):
                        logger.debug(f"Button {i}: {button.get_attribute('class')}")
        except Exception as e:
            raise Exception(f"Warning: Could not toggle web search: {e}")

    def _handle_enter_query_in_text_area(self, query):
        logger.debug("Submitting query...")
        textarea = self.page.locator('textarea')
        textarea.fill(query)
        textarea.press('Enter')

    def _handle_text_streaming(self, min_chat_start_time, start_time, max_wait_time, chat_stream_wait_time=1,
                               web_search=False, each_chunk_stream_delay=None):
        """
        Handle text streaming from the chat response, yielding new tokens as they arrive.

        Args:
            min_chat_start_time (int): Minimum time to wait before starting to check for responses
            start_time (float): Start time of the request
            max_wait_time (int): Maximum time to wait for response
            chat_stream_wait_time (int): Time to wait between checks

        Yields:
            str: New tokens as they arrive
        Returns:
            str: Complete response text at the end
        """
        unchanged_count = 0
        previous_text = ""
        time.sleep(min_chat_start_time)
        while True:
            try:
                # Get current response text
                response_element = self.page.locator('.prose').last
                current_text = response_element.inner_text()

                # Skip empty responses
                if not current_text:
                    time.sleep(chat_stream_wait_time)
                    continue

                # Yield only the new tokens
                if len(current_text) > len(previous_text):
                    new_tokens = current_text[len(previous_text):]
                    yield new_tokens

                # Check if response has stabilized
                if current_text == previous_text:
                    unchanged_count += 1
                    if unchanged_count >= 1:  # Check 3 times to ensure stability
                        self._handle_web_search_toggle(web_search)  # rehit to turn off websearch
                        break
                else:
                    unchanged_count = 0
                    previous_text = current_text

                # Check timeout
                if time.time() - start_time > max_wait_time:
                    self._handle_web_search_toggle(web_search)  # rehit to turn off websearch
                    break

                time.sleep(each_chunk_stream_delay)
            except Exception as e:
                logger.debug(f"Error while monitoring response: {e}")
                break

        return previous_text

    def _handle_click_new_chat_button(self):
        try:
            # Wait for element to be visible with timeout
            new_chat_button = self.page.get_by_role("link", name="New Chat").first

            # Add explicit wait for visibility
            try:
                new_chat_button.wait_for(state="visible", timeout=5000)  # 5 second timeout
                logger.debug("New chat button is visible. Clicking...")
                new_chat_button.click()
                time.sleep(1)
                logger.debug("Clicked successfully.")
            except Exception as e:
                logger.debug(f"Button wait timed out: {e}")

                # Fallback approach - try forcing the click even if not "visible"
                try:
                    logger.debug("Attempting force click...")
                    new_chat_button.click(force=True)
                    time.sleep(1)
                    logger.debug("Force click successful.")
                except Exception as e2:
                    logger.debug(f"Force click failed: {e2}")
                    # If both attempts fail, continue with the existing chat
                    logger.debug("Continuing with existing chat...")

        except Exception as e:
            logger.debug(f"Failed to handle new chat button: {e}")
            logger.debug("Continuing with existing chat...")
