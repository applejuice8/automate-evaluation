import pandas as pd
from playwright.sync_api import sync_playwright

class EvaluationBot:
    def __init__(self, headless=True):
        self.headless = headless

    def __enter__(self):
        self.play = sync_playwright().start()
        self.browser = self.play.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()
        return self

    def __exit__(self, *args):
        self.browser.close()
        self.play.stop()

    def goto(self, url):
        self.page.goto(url)
    
    def get_title(self):
        return self.page.locator('#survey_header').inner_text()

    def main(self):
        with open('links.txt', 'r') as f:
            urls = f.readlines()
            for url in urls:
                try:
                    self.goto(url)
                    title = self.get_title()
                except Exception as e:
                    print(f'Error encountered at {title}')
                    print(e)


