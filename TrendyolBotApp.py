from TrendyolLoginInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




class Trendyol:
    def __init__(self):
        self.browser=webdriver.Chrome()
        self.fiyatRepository=[]
        self.markaRepository=[]
        self.genelInfoRepository=[]
        
        
        

        
        
        
        
    def signIn(self):
        self.browser.get("https://www.trendyol.com")
        self.browser.maximize_window()  
        time.sleep(2)
        
        ilkSecim=self.browser.find_element_by_xpath("//*[@id='gender-popup-modal']/div/div/div[2]/div[2]/a/span[1]/img")
        ilkSecim.click()
        
        girisYap=self.browser.find_element_by_xpath("//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
        girisYap.click()
        
        eMail=self.browser.find_element_by_xpath("//*[@id='login-email']")
        eMail.send_keys(username)
        
        password=self.browser.find_element_by_xpath("//*[@id='login-password-input']")
        password.send_keys(password)
        
        time.sleep(2)
        
        girisButton=self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button")
        girisButton.click()
        
    
        
        

        
            


    def search(self):
                
        self.browser.get("https://www.trendyol.com")
        self.browser.maximize_window()  
        time.sleep(2)
        
        self.browser.searchInput=self.browser.find_element_by_css_selector(".search-box") 
        self.browser.searchInput.send_keys("Erkek giyim")
        self.browser.searchInput.send_keys(Keys.ENTER)
        
        boslugaTıklama=self.browser.find_element_by_xpath("//*[@id='container']/div[3]/div[2]/div[2]/div")
        boslugaTıklama.click()
        
        time.sleep(3)
        
        
        
        
        
    def scrolling(self):
        lastHeight=self.browser.execute_script("return document.documentElement.scrollHeight") ##scroll barın yüksekliği neyse onu döndürmek istiyoruz.
        
        sayac=3
        
        while True:
            if sayac>0: 
                
                self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight-2000);")
                
                time.sleep(2)
                newHeight=self.browser.execute_script("return document.documentElement.scrollHeight")
            
                ##Son yükseklik, newHeight'taki yüksekliğe eşitse artık daha yüklenecek bir şey kalmamış demektir ve bu durumda döngüyü bitirmemiz gerekir.
                if lastHeight==newHeight:
                    break
            
                else:
                    lastHeight=newHeight
                
                sayac-=1
            
            else:
                break
        
        
    
    
    
    
    def priceSearch(self):
        
        self.scrolling() 
            
        items=self.browser.find_elements_by_css_selector(".prc-box-sllng")
        count=len(items)
        print(f"first count: {count}")
        for item in items:
            self.fiyatRepository.append(item.text)
    
    
    
    def nameSearch(self):
        
        
        
        items=self.browser.find_elements_by_css_selector(".p-card-wrppr") ##Takipci kısmına sağtık incele yapıp ordan aldık.
        count=len(items)
        print(f"first count: {count}")
        
        for i in items:
            self.markaRepository.append(i.find_element_by_css_selector(".prdct-desc-cntnr-ttl").text)

            ##gitHub'ta fallowers kısmında sağtık incele yapıyoruz>div'i açıyoruz>a'yı açıyoruz>ordaki spann class'ı alıyoruz.
            
            
    def genelInfoSorgulama(self):
        
        
        items=self.browser.find_elements_by_css_selector(".p-card-wrppr") ##Takipci kısmına sağtık incele yapıp ordan aldık.
        count=len(items)
        print(f"first count: {count}")
        
        for i in items:
            self.genelInfoRepository.append(i.find_element_by_css_selector(".prdct-desc-cntnr").text)
            
            
    #def dataTexteEkleme(self):
        with open('C:\data11.txt','x') as myFile: # x'in anlamı create yapmaktır. Var olan bir text belgesine bunu uygularsak çalışmaz cünkü kendinin yeni bir text oluşturması bizim amacımız.
             myFile.write('Python 1\n')
             myFile.write('Django')
             
             
    def dataUpdate(self):
        with open('C:\data11.txt','a') as myFile:
            for name in self.fiyatRepository:
                myFile.write(name+"\n")
            

        
             
     

             
             
  
             
            
            
        
    
    #def autoRun(self):
        
            
        #schedule.every().day.at("23:33").do(Trendyol.signIn())
        #while True:
            #schedule.run_pending()
            
            
            
    
    

            
            

        
        
        
            
            
        
            



trndyol=Trendyol()
trndyol.signIn()
trndyol.search()    
#trndyol.fiyatSorgulama()
#trndyol.isimSorgulama()
trndyol.genelInfoSorgulama()
#trndyol.autoRun()
print(trndyol.markaRepository)
print(trndyol.genelInfoRepository)
print(trndyol.fiyatRepository)
#trndyol.dataTexteEkleme()
trndyol.dataUpdate()
















