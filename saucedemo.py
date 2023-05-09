from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

service = ChromeService(executable_path="chromedriver")
#driver = webdriver.Chrome(service=ChromeService(executable_path="chromedriver"))
driver = webdriver.Firefox(service=FirefoxService(executable_path="geckodriver"))

driver.get("https://www.saucedemo.com/")
#implicit wait
driver.implicitly_wait(10)
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
assert "Epic sadface: Sorry, this user has been locked out." in message