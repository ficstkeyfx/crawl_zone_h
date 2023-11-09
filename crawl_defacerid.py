# from turtle import position
import undetected_chromedriver as uc
import time
import os
import requests
from selenium.webdriver.chrome.options import Options
# start position 12466886
# print(requests.get(url).status_code)

class Crawler:
    url = 'https://defacer.id/archive/mirror/'

    def __init__(self,driver) -> None:
        self.driver = driver
    
    def crawl(self):
        position = self.get_pos('position_deface.txt')
        # print(po)
        print(self.url, position)
        self.driver.get(self.url + position)
        # self.driver.set_window_position(0,0)
        # self.driver.set_window_size(1024,768)
        time.sleep(35)
        # get_core_data
        self.dict_data = self.crawl_deface_id()
        # print(dict_data)
        # print(dict_data['url'])

        # 
        # pathSave = "E:/NC/001.Crawl_data/data"
        pathSave = "D:/NCKH/01_CrawlData/Mine/deface_data/"
        print(self.is_new_notified(self.dict_data['defacer']))
        try:
            if(self.is_new_notified(notified_name = self.dict_data['defacer'])):
                pathSaveCoreData = os.path.join(pathSave,'core_data')
                pathSaveImgData = os.path.join(pathSave,'image')
                pathSaveTextData = os.path.join(pathSave,'text')
                pathSaveHtmlData = os.path.join(pathSave,'html')
                self.writeResultCoreData(pathSaveCoreData)
                self.writeResultData(pathSaveImgData,pathSaveTextData,pathSaveHtmlData)
                self.write_new_notified(notified_name = self.dict_data['defacer'])
                self.reWritePos()
            else :
                self.reWritePos()
        except:
            self.reWritePos()
    def crawl_deface_id(self):
        list_data = self.driver.find_elements_by_tag_name('strong')
        list_data = [li.text for li in list_data]
        name = ['url','time','ip','defacer','system','team','web-server']
        return dict(zip(name,list_data))
    # crawl data
    def writeResultData(self,pathSaveImgData,pathSaveTextData,pathSaveHtmlData):
        # assert False
        domain = self.dict_data['url']
        
        if requests.get(domain).status_code != '404' and  requests.get(domain).status_code != '403':
            self.driver.get(domain)
            time.sleep(15)
            def write_img():
                self.driver.save_screenshot(os.path.join(pathSaveImgData,self.pos+".png"))
            def write_text():
                el = self.driver.find_element_by_tag_name('html')
                with open(os.path.join(pathSaveTextData,self.pos+".txt"),'w') as file:
                    file.write(el.text) 
                with open(os.path.join(pathSaveHtmlData,self.pos+'.html'),'w') as file :
                    # print(1)
                    file.write(self.driver.page_source)
            write_img()
            write_text()
    
    def writeResultCoreData(self,path):
        file = open(os.path.join(path,self.pos+".txt"),'w')
        core = [value for key, value in self.dict_data.items()]
        # print(core)
        for cor in core :
            file.write(cor+",")
        file.close()

    def write_new_notified(self, notified_name):
        # notified_name = self.get_notified()
        with open('old_notified_deface_id.txt','a') as file:
            file.write(notified_name)
            file.write('\n')

    #position
    def get_pos(self,fileNameOfPos):
        self.fileNameOfPos = fileNameOfPos
        with open(fileNameOfPos,'r') as file:
            self.pos = file.read()
        return self.pos
    def reWritePos(self):
        cur_pos = int(self.pos) + 1
        with open(self.fileNameOfPos , 'w') as file:
            file.write(str(cur_pos))
    #notified
    def get_old_notified(self):
        with open('old_notified_deface_id.txt','r') as file:
            tmp = file.read()
            self.list_old_notified = tmp.split('\n')
        return self.list_old_notified
    def is_new_notified(self, notified_name):
            # notified_name = self.get_notified()
            old_notified = self.get_old_notified()
            #  = self.list_old_notified
            print(old_notified)
            print(notified_name)
            if old_notified == None:
                return True
            if notified_name not in old_notified :
                return True
            else:
                return False 
if __name__ == '__main__':
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = uc.Chrome(options=chrome_options)
    Cr = Crawler(driver)
    while True:
        Cr.crawl()