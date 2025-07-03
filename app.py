from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Scraper():
    def __init__(self, headless):
        options = Options()
        if headless:
            options.add_argument('--headless')  # Run in headless mode
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')  # Set window size to avoid layout issues

        self.driver = webdriver.Chrome(options=options)
    
    def get_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)
        self.main()

    def main(self):
        table = self.driver.find_element(By.XPATH, '//table[@class="clp_sv_matrix_table"]')
        questions = table.find_elements(By.XPATH, './/tr[@class="subquestion"]')
        
        for question in questions:
            choices = question.find_elements(By.XPATH, './/input[@type="radio"]')
            choices[-2].click()
        
        # Switch to iframe
        iframe = self.driver.find_element(By.XPATH, '//iframe')
        self.driver.switch_to.frame(iframe)

        # Find textarea
        textarea = self.driver.find_element(By.ID, 'tinymce')
        time.sleep(1)
        textarea.send_keys('ok')

        # Switch back
        self.driver.switch_to.default_content()

        # Submit
        submit = self.driver.find_element(By.ID, 'submit0')
        submit.click()

if __name__ == '__main__':
    url = input('URL: ')
    scraper = Scraper(headless=False)
    scraper.get_page(url)
