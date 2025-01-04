# _hf.py
import asyncio
import random
import sys
import time
from datetime import datetime
from loguru import logger

logger.remove()
logger.add(sys.stderr, level='CRITICAL')


class HuggingFaceAutomation:
    def __init__(self, browser_session):
        self.session = browser_session
        self.page = browser_session.page
        self.prev_conv_id:str = ""

    async def generate(self, query: str, system_prompt: str = "", web_search: bool = False,
                       max_wait_time: int = 300,
                       conversation_id:str = ""
                       ) -> str:
        async for chunk in self.stream_query(query, web_search, max_wait_time,
                                             system_prompt=system_prompt):
            yield chunk

    async def complete(self, query: str, system_prompt: str = "", web_search: bool = False,
                       max_wait_time: int = 300,
                       conversation_id: str = ""
                       ) -> str:
        result = []
        async for chunk in self.stream_query(query, web_search, max_wait_time,
                                             system_prompt=system_prompt,
                                             conversation_id=conversation_id):
            result.append(chunk)
        return "".join(result)

    async def web_search_button(self, web_search):
        if not web_search:
            return
        try:
            search_button = self.page.locator('button.base-tool.svelte-10z3gx0').first
            if await search_button.is_visible():
                await search_button.click()
                await asyncio.sleep(1)
            else:
                search_area = self.page.locator('div.group/tooltip.inline-block.md:relative').first
                if await search_area.is_visible():
                    await search_area.click()
                    await asyncio.sleep(1)
        except Exception as e:
            raise Exception(f"Warning: Could not toggle web search: {e}")

    async def write_and_chat(self, query, web_search):
        await self.web_search_button(web_search)
        textarea = self.page.locator('textarea')
        await textarea.fill(query)
        await textarea.press('Enter')

    async def write_system_prompt(self, prompt: str) -> None:
        """Set the system prompt in the settings textarea."""

        #start by new chat
        await self.click_new_chat()

        logger.debug("Setting system prompt")
        settings_selectors = [
            'a[aria-label="Settings"]',
            'button[aria-label="Settings"]',
            '.btn.ml-auto.flex.h-7.w-7.self-start.rounded-full',  # Based on the screenshot
            '[class*="settings"]'
        ]

        settings_button = None
        for selector in settings_selectors:
            try:
                settings_button = self.page.locator(selector).first
                if await settings_button.is_visible(timeout=2000):
                    logger.debug(f"Found settings button: {selector}")
                    break
            except Exception:
                continue

        if not settings_button:
            raise Exception("Could not find settings button")

        await settings_button.click()
        await asyncio.sleep(1)  # Wait for modal animation

        # Try multiple possible selectors for the system prompt textarea
        textarea_selectors = [
            'textarea[aria-label="Custom system prompt"]',
            'textarea[placeholder*="system prompt"]',
            'textarea[class*="system-prompt"]'
        ]

        textarea = None
        for selector in textarea_selectors:
            try:
                textarea = self.page.locator(selector)
                if await textarea.is_visible(timeout=2000):
                    logger.debug(f"Found system prompt textarea: {selector}")
                    break
            except Exception:
                continue

        if not textarea:
            raise Exception("Could not find system prompt textarea")

        await textarea.fill(prompt)
        await asyncio.sleep(1)

        await self.page.mouse.click(10, 10)
        await asyncio.sleep(2)
        logger.info(f"System prompt set successfully: {prompt[:50]}...")

    async def stream_query(self, query, web_search=False, max_wait_time=300, system_prompt="",
                            conversation_id: str = ""
                           ):
        logger.debug(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing query: {query[:50]}...")

        """
        if current convid is empty:
            perform write system prompt and write_chat 
        else if current convid is not empty:
            if current convid is different from previous convid:
                perform write system prompt and write_chat 
            else if current convid is same as previous convid:
                only write_chat
        """
        if (self.prev_conv_id!=conversation_id) or conversation_id=="":
            await self.write_system_prompt(system_prompt)

        self.prev_conv_id = conversation_id

        await self.write_and_chat(query, web_search=web_search)

        min_chat_start_time = 1 + (7 if web_search else 0)
        await asyncio.sleep(min_chat_start_time)

        async for chunk in self.stream_text_logic(web_search=web_search, max_wait_time=max_wait_time):
            yield chunk

    async def stream_text_logic(self, web_search=False, max_wait_time=300):
        unchanged_count = 0
        start_time = time.time()
        last_length = 0  # Track the last length instead of storing full previous text

        while True:
            try:
                response_element = self.page.locator('.prose').last
                current_text = await response_element.inner_text()

                if not current_text:
                    await asyncio.sleep(0.5)
                    continue

                current_length = len(current_text)

                if current_length > last_length:
                    new_content = current_text[last_length:]
                    yield new_content

                # Check if response is complete (no changes in last 2 checks)
                if current_length == last_length:
                    unchanged_count += 1
                    if unchanged_count >= 3:
                        await self.web_search_button(web_search)
                        logger.debug(f'Stopping reason unchanged_count: {unchanged_count}')
                        break
                else:
                    unchanged_count = 0

                last_length = current_length

                if time.time() - start_time > max_wait_time:
                    await self.web_search_button(web_search)
                    break

                await asyncio.sleep(1)
            except Exception as e:
                logger.debug(f"Error while monitoring response: {e}")
                break

    async def click_new_chat(self):
        try:
            new_chat_button = self.page.get_by_role("link", name="New Chat").first
            try:
                await new_chat_button.wait_for(state="visible", timeout=5000)
                await new_chat_button.click()
                await asyncio.sleep(1)
            except Exception as e:
                try:
                    await new_chat_button.click(force=True)
                    await asyncio.sleep(1)
                except Exception as e2:
                    logger.debug(f"Force click failed: {e2}")
        except Exception as e:
            logger.debug(f"Failed to handle new chat button: {e}")


async def main():
    from liteauto.async_playwright._session import HFBrowserSession
    session = await HFBrowserSession.create(headless=False)
    auto = HuggingFaceAutomation(session)
    queries = [
        ("your name is santhosh", 'what is your name'),
        ("your name is mahesh", "what is your name"),
        ("your name is ramesh", "what is your name"),
        ("your name is krishna", "what is your name"),
        ("your name is rajesh", "what is your name"),
        ("your name is anil", "what is your name"),
        ("your name is sudhir", "what is your name"),

    ]
    q = random.choice(queries)
    res = await auto.complete(q[1], system_prompt=q[0])
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
