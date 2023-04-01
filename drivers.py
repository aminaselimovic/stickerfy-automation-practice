from selenium import webdriver

def headlessChrome():
    from selenium.webdriver.chrome.service import Service
    servObj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.headless = True
    option.add_experimental_option('excludeSwitches', ['enable-logging']) 
    driver = webdriver.Chrome(service=servObj, options=option)
    return driver

def headlessEdge():
    from selenium.webdriver.edge.service import Service
    servObj = Service("C:\Drivers\edgedriver_win32\msedgedriver.exe") #fix this
    option = webdriver.EdgeOptions()
    option.headless = True
    option.add_experimental_option('excludeSwitches', ['enable-logging']) 
    driver = webdriver.Edge(service=servObj, options=option)
    return driver

def headlessFirefox():
    from selenium.webdriver.firefox.service import Service
    servObj = Service("C:\Drivers\geckodriver-v0.32.0-win64\geckodriver.exe") #fix this
    option = webdriver.FirefoxOptions()
    option.headless = True
    option.add_experimental_option('excludeSwitches', ['enable-logging']) 
    driver = webdriver.Firefox(service=servObj, options=option)
    return driver
