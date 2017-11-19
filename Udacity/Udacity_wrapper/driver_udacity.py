from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.udacity.com/courses/all'
driver = webdriver.Firefox()
driver.set_page_load_timeout(1200)
driver.get(url)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
courseTags = soup.find_all("div", "course-summary-card row row-gap-medium")
courselist = []
domain = 'https://www.udacity.com'
i = 0
for tag in courseTags:
    coursedic = {}
    i += 1
    coursedic["id"] = "udacity" + str(i).zfill(5)
    coursedic["provenance"] = "udacity"
    coursedic["img"] = tag.select('img[src]')[0]['data-src']
    coursedic["course_url"] = domain + tag.select('a[data-course-title]')[0]['href']
    coursedic["name"] = tag.select('a[data-course-title]')[0]\
    .text.strip().decode('utf8').encode('ascii', errors='ignore')
    coursedic["description"] = tag.select('div[data-course-short-summary]')[0]\
    .text.strip().decode('utf8').encode('ascii', errors='ignore')
    courselist.append(coursedic)
driver.quit()

print courselist
with open('../udacity_data.json', 'a') as f:
    json.dump(courselist, f)