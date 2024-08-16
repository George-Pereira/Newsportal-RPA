
class RelevantNews:
    def __init__(self, headline:str, news_date:str, description:str, picture_path: str, ismoneyrelated:bool):
        self.__headline = headline
        self.__news_date = news_date
        self.__picture_path = picture_path
        self.__ismoneyrelated = ismoneyrelated
        self.__description = description
        pass
    def getHeadline(self):
        return self.__headline
    def setHeadline(self, headline):
        self.__headline = headline
    def getNewsdate(self):
        return self.__news_date
    def setNewsdate(self, news_date):
        self.__news_date = news_date
    def getPicturepath(self):
        return self.__picture_path
    def setPicturepath(self, picture_path):
        self.__picture_path = picture_path
    def getIsmoneyrelated(self):
        return self.__ismoneyrelated
    def setIsmoneyrelated(self,Ismoneyrelated):
        self.__ismoneyrelated = Ismoneyrelated
    def getDescription(self):
        return self.__description
    def setDescription(self, description):
        self.__description = description