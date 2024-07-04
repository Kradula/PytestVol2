from selenium import webdriver


class TestYoutube:

    def test_youtube_title(self):

        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/")

        assert driver.title == "YouTube"
