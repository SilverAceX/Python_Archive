from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from person import *

def get_list(street, city):
    chrome_options = Options()
    #chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(r"C:\Users\terer\.wdm\drivers\chromedriver\win32\95.0.4638.17\chromedriver.exe", chrome_options=chrome_options)
    browser.get("http://www.canada411.ca")
    browser.find_element_by_link_text("More search options").click()
    browser.find_element_by_link_text("Reverse address").click()
    #time.sleep(4)
    browser.find_element_by_xpath('//*[@id="c411AddressCity"]').send_keys(street)
    browser.find_element_by_xpath('//*[@id="AddressSearch"]/div/div[2]/input').send_keys(city)
    browser.find_element_by_xpath('//*[@id="AddressSearch"]/div/div[3]/select/option[10]').click()
    browser.find_element_by_xpath('//*[@id="c411AddressFind"]').click()
    #time.sleep(1)
    numResults = browser.find_element_by_xpath('//*[@id="c411Body"]/div[2]/div[1]/div[3]/div[1]/h1').text.split()[0]
    if "," in numResults:
        numResults = numResults.split(",")
        numResults = "".join(numResults)
    numResults = int(numResults)
    complete_list = []
    count = 1
    for i in range(1, numResults+1):
        
        c1 = 'ContactName{}'.format(count)
        c2 = 'ContactPhone{}'.format(count)
        c3 = 'ContactAddress{}'.format(count)

        #time.sleep(1)
        name = browser.find_element_by_id(c1).text
        phone = browser.find_element_by_id(c2).text
        address = browser.find_element_by_id(c3).text

        complete_list.append(Person(name,phone,address))

        
        if (count/15 == count//15):
            count = 0
            #time.sleep(1)
            try:
                browser.find_elements_by_link_text('Next')[0].click()
            except:
                print()
    
        count += 1
    return complete_list
