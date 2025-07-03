# Selenium Survey Scraper

This project is a simple web scraper that automates form filling and submission using Selenium.

## 🔧 Features

- Automatically selects radio button responses in a survey table.
- Enters a response in a TinyMCE editor inside an iframe.
- Submits the form.
- Optionally runs in headless mode.

## 📦 Requirements

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (installed and available in system PATH)

## 📁 Installation

1. Clone or download this repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Optional: Use `webdriver-manager` to avoid managing ChromeDriver manually

Uncomment the following in your script:
```python
# from webdriver_manager.chrome import ChromeDriverManager
# self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
```

Then add this to your `requirements.txt`:
```txt
webdriver-manager
```

## 🚀 Usage

```bash
python your_script_name.py
```

You will be prompted to input the survey page URL.

## ⚙️ Headless Mode

To run without opening the browser window, change this line in your script:

```python
scraper = Scraper(headless=True)
```

## 🧠 Notes

- The script locates a table with radio inputs and selects second-to-last option in each row.
- It handles TinyMCE editors inside iframes.
- Implicit waits are used to reduce timing issues.

## 📄 License

MIT License
