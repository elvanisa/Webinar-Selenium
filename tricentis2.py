import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.locator import elem
from pageObject.data import inputan

class TestWebinar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, elem.loginBtn).click()
        driver.find_element(By.ID, elem.email).send_keys(inputan.valid_email)
        driver.find_element(By.ID, elem.password).send_keys(inputan.valid_password)
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
        driver.find_element(By.XPATH, "//h2[@class='product-title']//a[contains(text(),'$25 Virtual Gift Card')]").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/25-virtual-gift-card")

    def test_failed_login(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, elem.loginBtn).click()
        driver.find_element(By.ID, elem.email).send_keys(inputan.invalid_email)
        driver.find_element(By.ID, elem.password).send_keys(inputan.invalid_password)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()