from tracemalloc import start
from webbrowser import Chrome
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import undetected_chromedriver as uc
class crawlBySeleniumZoneh :
    PATH = "C:/chromedriver.exe"
    url = "https://zone-h.org/mirror/id/"
    is_silent = False
    list_old_notified = []
    def crawlAndWriteData(self,pathSave,filePathOfPos = "position.txt"):
        # print(1)
        self.get_pos(filePathOfPos)
        self.url = "https://zone-h.org/mirror/id/"
        self.url += self.pos 
        # 
        pathSaveCoreData = os.path.join(pathSave,'core_data')
        pathSaveImgData = os.path.join(pathSave,'image')
        pathSaveTextData = os.path.join(pathSave,'text')
        pathSaveHtmlData = os.path.join(pathSave,'html')
        try:
            self.crawl_deface_id()
        # time.sleep(1100)
            print(self.is_new_notified())
            if self.is_new_notified():
                print(self.list_old_notified)
                self.writeResultCoreData(pathSaveCoreData)
                self.writeResultData(pathSaveImgData,pathSaveTextData,pathSaveHtmlData)
                self.write_new_notified()
                # self.WriteResultTxtData(pathSaveTextData)
            self.reWritePos()
        except:
            # print(self.is_new_notified())
            self.reWritePos()

    def start(self,path=""):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_argument('--start-maximized')
        if(self.is_silent):
            option.add_argument("--headless")
        # Pass the argument 1 to allow and 2 to block
        # option.add_experimental_option("prefs", { 
        #     "profile.default_content_setting_values.notifications": 2 
        # })
        self.driver = webdriver.Chrome(executable_path=self.PATH)

    def get_pos(self,fileNameOfPos):
        with open(fileNameOfPos,'r') as file:
            self.pos = file.read()

    def __init__(self, pathChromedriver = "C:/chromedriver.exe",filePathOfPos = "position.txt") :
        self.PATH = pathChromedriver 
        self.fileNameOfPos = filePathOfPos
        self.start(self.PATH)
            
    

    def crawl_deface_id(self):
        self.driver.get(self.url)
        tags = self.driver.find_elements_by_class_name("deface0")
        try:
            self.driver.find_element_by_id_name("cryptogram")
            return None
        except:
            # for tag in tags :
            #     print(tag.text)
            print(1111)
            infor = tags[1].text
            self.inforOfZoneh = infor 
            return infor
            time.sleep(30)
        
    def reWritePos(self):
        cur_pos = int(self.pos) + 1
        with open(self.fileNameOfPos , 'w') as file:
            file.write(str(cur_pos))

    def writeResultCoreData(self,path):
        file = open(os.path.join(path,self.pos+".txt"),'w')
        file.write(self.inforOfZoneh)
        file.close()
    
    def get_notified(self):
        notified_name = self.inforOfZoneh.split('\n')[0]
        return notified_name

    def get_old_notified(self):
        with open('old_notified.txt','r') as file:
            tmp = file.read()
            self.list_old_notified = tmp.split('\n')
        return 

    def is_new_notified(self):
        notified_name = self.get_notified()
        self.get_old_notified()
        old_notified = self.list_old_notified
        if old_notified == None:
            return True
        if notified_name not in old_notified :
            return True
        else:
            return False

    def get_domain(self):
        core_data = self.inforOfZoneh.split('\n')
        domain = core_data[1].split(' ')[1]
        return domain

    def write_new_notified(self):
        print(11111111)
        notified_name = self.get_notified()
        with open('old_notified.txt','a') as file:
            file.write(notified_name)
            file.write('\n')

    

    def writeResultData(self,pathSaveImgData,pathSaveTextData,pathSaveHtmlData):
        # assert False
        domain = self.get_domain()
        self.driver.get(domain)
        time.sleep(5)
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
        try:
            write_text()
        except:
            return



    