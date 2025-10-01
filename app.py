from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Evaluator():
    def __init__(self, headless):
        options = Options()
        if headless:
            options.add_argument('--headless=new')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=service)

    def prompt_stars(self):
        while True:
            inp = input('How many stars (1-5)?')
            if inp.isdigit():
                n_stars = int(inp)
                if 1 <= n_stars <= 5:
                    break
            print('Invalid stars. Please enter a value between 1-5.')
        return n_stars

    def prompt_comment(self):
        while True:
            comment = input('Enter comment: ')
            if comment.strip():
                break
            print('Invalid comment. Please enter at least 1 character.')
        return comment

    def prompt_values(self):
        n_stars = self.prompt_stars()
        comment = self.prompt_comment()
        return (n_stars, comment)

    def read_links(self, filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def get_page(self, url):
        self.driver.get(url)

    def rate_stars(self, n_stars):
        questions = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="clp_sv_matrix_table"]//tr[@class="subquestion"]'))
        )

        for question in questions:
            stars = question.find_elements(By.XPATH, './/input[@type="radio"]')
            stars[n_stars - 1].click()

    def fill_comment(self, comment):
        # Switch to iframe
        iframe = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//iframe'))
        )
        self.driver.switch_to.frame(iframe)

        # Type comment
        self.driver.find_element(By.ID, 'tinymce').send_keys(comment)

        # Switch back
        self.driver.switch_to.default_content()

    def submit(self):
        self.driver.find_element(By.ID, 'submit0').click()

    def main(self):
        urls = self.read_links('links.txt')

        for url in urls:
            try:
                self.get_page(url)
                n_stars, comment = self.prompt_values()
                self.rate_stars(n_stars)
                self.fill_comment(comment)
                self.submit()
            except Exception as e:
                print(f'Error encountered for link "{url}": {e}')
        self.driver.quit()

if __name__ == '__main__':
    evaluator = Evaluator(headless=False)
    evaluator.main()
