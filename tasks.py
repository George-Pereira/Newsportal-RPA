from robocorp.tasks import task
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from Browser import Browser
from Excel import Excel
from RelevantNews import RelevantNews
from datetime import datetime

Set_Selenium_Speed = 0.5

@task
def minimal_task():
    print("iniciando")
    start = Browser()
    start.setSearchTerm("money")
    workbook = Excel("")
    workbook.setFilename("LATimes-extraction-" + datetime.today().date().__str__() + "-" + datetime.today().second.__str__() + ".xlsx")
    workbook.getWorkbook().save(workbook.getFilename().__str__())
    def setUpExcel(self:Excel):
                workbook = self.getWorkbook().active
                workbook.title = "LATimes_Extraction"
                workbook['A1'] = "Headline"
                workbook['B1'] = "Description"
                workbook['C1'] = "News Date"
                workbook['D1'] = "Mentions Money?"
                workbook['E1'] = "Picture Path"
    def retrieve_relevant_news(self:Browser, workbook:Excel):
        try:
            today_time = datetime.today().date()
            print("today's timestamp is = " + str(today_time))
            content_cursor = self.getWait().until(EC.url_contains("&s=1"))
            self.getWait().until(EC.staleness_of(self.getWait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "ps-search-filters > div > main > ul > li")))))
            content_cursor = self.getWait().until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ps-search-filters > div > main > ul > li")))
            print("news amount found = " + str(len(content_cursor)))
            for news in content_cursor:
                news_date = news.find_element("css selector", "ps-promo > div > div.promo-content > p.promo-timestamp").get_attribute("data-timestamp")
                print("The News Timestamp is = " + news_date)
                news_date = datetime.fromtimestamp(float(news_date)/1000)
                date_difference = today_time - news_date.date()
                print("The News difference is = " + str(date_difference.days))
                if date_difference.days<=30: 
                    relatedNews = RelevantNews("","","","",False)
                    relatedNews.setHeadline(news.find_element("css selector", "ps-promo > div > div.promo-content > div > h3 > a").get_attribute("innerHTML"))
                    relatedNews.setNewsdate(str(news_date.date()))
                    relatedNews.setDescription(news.find_element("css selector", "ps-promo > div > div.promo-content > p.promo-description").get_attribute("innerHTML"))
                    relatedNews.setPicturepath(news.find_element("css selector", "ps-promo > div > div.promo-media > a > picture > img").get_attribute("src"))
                    self.getMyBrowser().execute_script(f"window.open('" + relatedNews.getPicturepath().__str__() + "', 'second_tab')")
                    self.getMyBrowser().switch_to.window("second_tab")
                    self.getMyBrowser().get(relatedNews.getPicturepath())
                    self.getWait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > img")))
                    self.getMyBrowser().save_screenshot(relatedNews.getHeadline().replace(" ", "_").replace(":", "").replace(".", "").replace("'", "") + ".png")
                    self.getMyBrowser().switch_to.window(self.getMyBrowser().window_handles[0])
                    self.getMyBrowser().execute_script(f"window.close('second_tab')")
                    relatedNews.setPicturepath(relatedNews.getHeadline().replace(" ", "_").replace(":", "").replace(".", "").replace("'", "") + ".png")
                    print("image path = " + relatedNews.getPicturepath())
                    if relatedNews.getHeadline().__contains__("$") or relatedNews.getHeadline().__contains__("dollars") or relatedNews.getHeadline().__contains__("USD"):
                        relatedNews.setIsmoneyrelated(True)
                    else:
                        relatedNews.setIsmoneyrelated(False)
                        write_in_excel(relatedNews, workbook)
        except StaleElementReferenceException as stalerror:
            print(str(stalerror))
            retrieve_relevant_news(self, workbook)
    pass
    def navigate_newsportal(self:Browser):
        
        try:
            current_cursor = self.getWait().until(EC.presence_of_element_located((By.XPATH, '/html/body/ps-header/header/div[2]/button')))
            current_cursor.click()
            current_cursor = self.getWait().until(EC.element_to_be_clickable((By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')))
            current_cursor.click()
            current_cursor.send_keys(self.getSearchTerm() + Keys.RETURN)
            current_cursor = self.getWait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "select > option:nth-child(2)"))).click()
        finally:        
            print("Navigation completed")
        pass
    def write_in_excel(self:RelevantNews, workbook:Excel):
            active_workbook = workbook.getWorkbook().active
            active_workbook.append([self.getHeadline().__str__(), self.getDescription().__str__(), self.getNewsdate().__str__(), self.getIsmoneyrelated().__str__(), self.getPicturepath().__str__()])
            workbook.getWorkbook().save(workbook.getFilename().__str__())
    pass
    setUpExcel(workbook)
    navigate_newsportal(start)
    retrieve_relevant_news(start, workbook)