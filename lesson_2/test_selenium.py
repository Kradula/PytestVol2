from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

LOGIN_PAGE = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
MAIN_MENU_PAGE = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


class TestLogin:

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(driver=self.driver, timeout=10)

    def test_go_to_url(self, url=LOGIN_PAGE):
        self.driver.get(url)

        assert self.driver.current_url == url

    def test_username(self, username="Admin"):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        username_field = self.driver.find_element(*self.USERNAME_FIELD)
        username_field.send_keys(username)

        assert username_field.get_attribute("value") == username, "Names are not equal."

    def test_password(self, password="admin123"):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))

        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

        assert password_field.get_attribute("value") == password, "Passwords are not equal."

    def test_button_login(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        button_field = self.driver.find_element(*self.LOGIN_BUTTON)
        button_field.click()

    def test_is_logined(self, url=LOGIN_PAGE):
        self.wait.until(EC.url_changes(url))

        assert self.driver.current_url == MAIN_MENU_PAGE, "Links are not match."

    def teardown_class(self):
        self.driver.quit()
