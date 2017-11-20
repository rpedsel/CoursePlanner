from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# _x_query = {
#         "coursetag": "//div[@class = 'gs-webResult gs-result']", 
#         "coursename":   "//a[@class='gs-title']", 
#         "description": "//div[@class = 'gs-bidi-start-align gs-snippet']"
#         "image_url": "//img[@class='gs-image']", 
#         }

def wrapper(url, id):
    # source_code = requests.get(url)
    # plain_text = source_code.text
    # soup = BeautifulSoup(plain_text, 'html.parser')
    browser = webdriver.Firefox()
    browser.set_page_load_timeout(1200)
    browser.get(url)
    courselist = browser.find_elements_by_xpath('//div[@class = "gs-webResult gs-result"]')
    list = []
    for course in courselist:
        coursedic = {}
        coursedic["id"] =  "khan" + str(id).zfill(5)
        coursedic["description"] = course.text.split('\n')[-1]
        coursedic["name"] = course.text.split('\n')[0].split('|')[0]
        coursedic["provenance"] = "khan Academy"
        if coursedic["name"] == "" or coursedic["description"] == "":
            continue
        id += 1
        list.append(coursedic)
    urls = [i.get_attribute('href') for i in browser.find_elements_by_xpath("//div/a[@class='gs-image']")]
    images = [i.get_attribute('src') for i in browser.find_elements_by_xpath("//img[@class='gs-image']")]
    alist = []
    for i in range(len(list)):
        if i < len(urls) and i < len(images):
            course = list[i]
            course["course_url"] = urls[i]
            course["img"] = images[i]
            alist.append(course)
    browser.close()
    return id, alist
    # print data



def driver(domain, keywords, data, i):
    for keyword in keywords:
        print keyword
        url = domain + keyword
        print url
        browser = webdriver.Firefox()
        browser.set_page_load_timeout(1200)
        browser.get(url)
        time.sleep(20)
        for j in range(1, 9):
            pages = browser.find_elements_by_xpath('//div[@class = "gsc-cursor-page"]')
            if j < len(pages):
                page = pages[j]
                page.click()
                time.sleep(40)
                result = wrapper(url, i)
                data += result[1]
                i = result[0]
                # pages = browser.find_elements_by_xpath('//div[@class = "gsc-cursor-page"]')
            else:
                break
        browser.close()
    browser.close()

domain = "https://www.khanacademy.org/search?referer=%2F&page_search_query="
keywords = ['data', 'social' 'marketing', 'design', 'web', 'cyber']
#,\
#  'program', 'platform', 'map', 'intelligence', 'knowledge', 'graph', 'probability',\
#   'digital', 'electronic', 'architecture', 'infrastructure', 'digital', 'electronic',\
#    'architecture', 'infrastructure', 'program', 'platform', 'map', 'intelligence',\
#     'entrepreneurship','cyber', 'knowledge', 'graph', 'probability', "engineer"]
i = 0
data = []
driver(domain, keywords, data, i)
# browser.quit()



with open('khan_data.json', 'a') as f:
    json.dump(data, f)