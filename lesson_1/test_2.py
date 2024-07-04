from selenium import webdriver


class TestPythonTutor:

    def test_python_tutor_title(self):
        driver = webdriver.Chrome()
        driver.get("https://pythontutor.com/")

        assert driver.title == ("Online Python Tutor - visualize, debug, get AI help for "
                                "Python, Java, C, C++, and JavaScript")
