from requests.api import request
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


bright_Stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome("C:\chromedriver")
browser.get(bright_Stars_url)
time.sleep(10)

def scrape():
    page = request.get(bright_Stars_url)
    star_data = []
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for th_tag in soup.find_all("th" , attrs={"class","headerSort"}):
        tr_tags = th_tag.find_all("tr")
        temp_list = []
        #Enumerate is a function that returns the index along with the element.
        for index , tr_tag in enumerate(tr_tags):
            if index ==0:
                temp_list.append(tr_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append("/html/body/div[3]/div[3]/div[5]/div[1]/table/thead/tr/th[1]/a")
            
            star_data.append(temp_list)
        browser.find_element_by_xpath("").click()
    
    with open("scraper1.csv","w") as f:
        c = csv.writer(f)
        c.writerow(page)
        c.writerows(star_data)

scrape()