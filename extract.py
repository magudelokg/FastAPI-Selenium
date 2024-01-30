from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver


def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://secure.technicaltraffic.com/carrier/CarrierInquiry.aspx")
    return driver.page_source


def doBackgroundTask():
    print("Doing background task")
    driver = createDriver()
    homepage = getGoogleHomepage(driver)
    driver.close()
    # print(inp.msg)
    print("Done")
    optimizer_path = r'C:\KGLogix\Python\Optimization\Scripts\main\main.exe'
    process_file = r"C:\KGLogix\Python\Optimization\ProcessFiles\test.json"

    # subprocess.call([r"C:\python_apps\ttc_bot\output\ttc_bot\ttc_bot.exe", "mposada@lean-tech.io"])
