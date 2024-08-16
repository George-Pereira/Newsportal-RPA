from RPA.Browser.Selenium import selenium_webdriver
from RPA.Browser.Selenium import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Set_Selenium_Speed = 0.5
class Browser(object):
    def __init__(self):
        self.__browser_options = Options()
        self.__my_browser = selenium_webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__browser_options)
        self.__wait = WebDriverWait(self.__my_browser, 30)
        self.__my_browser.get("https://www.latimes.com")
        self.__my_browser.maximize_window()
        self.__dateinterval = self

    def getSearchTerm(self):
        return self.__search_term
    def setSearchTerm(self, search_term):
        self.__search_term = search_term
        pass
    def getMyBrowser(self):
        return self.__my_browser
    def setMyBrowser(self):
        self.__my_browser = self
    def getBrowserOptions(self):
        return self.__browser_options
    def setBrowserOptions(self):
        self.__browser_options = self
    def getWait(self):
        return self.__wait
    def setWait(self):
        self.__wait = self
    def getDateinterval(self):
        return self.__dateinterval
    def setDateinterval(self):
        self.__dateinterval = self