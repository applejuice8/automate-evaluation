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

    def main(self):
        with open('links.txt', 'r') as f:
            lines = f.readlines()

