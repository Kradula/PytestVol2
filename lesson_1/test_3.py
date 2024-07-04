from selenium import webdriver


class TestAmazon:

    def test_amazon_title(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com/")

        assert driver.title == "Amazon.com"
