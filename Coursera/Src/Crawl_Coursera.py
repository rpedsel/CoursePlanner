from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

_x_query = {
        "coursename":   "//h2[@class = 'color-primary-text headline-1-text flex-1']", 
        "specialize":   "//span[@class = 'specialization-course-count']/span",
        "image_url":    "//div[@class='horizontal-box']/div/img", 
        "provenance": ["//span[@class = 'text-light offering-partner-names']/span", "//div[@class = 'text-light offering-partner-names']/span"]
    }


content = []
id = 0
# 4-skip 5
for j in range(11, 42):
    url = "https://www.coursera.org/courses?languages=en&query=web&start=" + str(j * 20)
    print url
    browser = webdriver.Firefox()
    browser.set_page_load_timeout(60)
    browser.get(url)
    time.sleep(20)
    # each page has 20 courses
    # coursename = [item.text.encode('ascii','ignore') for item in browser.find_elements_by_xpath(_x_query["coursename"])]
    # image = [item.get_attribute('src').encode('ascii','ignore') for item in browser.find_elements_by_xpath(_x_query["image_url"])]
    # provenance = [item.text.encode('ascii','ignore') for item in browser.find_elements_by_xpath(_x_query["provenance"][0])]
    # # provenance += [item.text.encode('ascii','ignore') for item in browser.find_elements_by_xpath(i for i in _x_query["provenance"[1]])]
    # specialize = [item.text.encode('ascii','ignore') for item in browser.find_elements_by_xpath(_x_query["specialize"])]
    # # store course info for each page
    

    # for i in range(len(coursename)):
    #     coursedic[coursename[i]] = {"image": image[i], "provenance": provenance[i]}

    # track the links corresponding to 20 courses

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    courseTags = soup.find_all("div", "offering-content")
    page = []
    for tag in courseTags:
        coursedic = {}
        coursedic["img"] = tag.select('img[src]')[0]['src']
        coursedic["name"] = tag.select('h2')[0].text.decode('utf8').encode('ascii', errors='ignore')
        specialization = tag.select('.specialization-course-count')
        if len(specialization) != 0:
            coursedic["specialization"] = True
        else:
            coursedic["specialization"] = False
        coursedic["provenance"] = tag.find_all('span')[-1].text.decode('utf8').encode('ascii', errors='ignore')
        page.append(coursedic)


    url_list = json.loads(soup.select_one("script[type=application/ld+json]").text)
    urls = [object['url'].encode('ascii','ignore') for object in url_list["itemListElement"]]
    urls = ["http:/" + url[4:] for url in urls]
    # urls of 20 courses respectively
    for i in range(len(urls)):
        browser.set_page_load_timeout(60)
        browser.get(urls[i])
        time.sleep(20)
        courseObject = page[i]
        courseObject["course_url"] = urls[i]
        # specialization
        source_code = requests.get(urls[i])
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        if 'specializations' in urls[i]:
            courseObject["courseSet"] = []
        # if courseObject["specialization"]:
            # descriptions = browser.find_elements_by_xpath('//div[@class="description-cont"]/div/div/span')
            desc = soup.find_all("div", "description subsection")
            if len(desc) != 0:
                courseObject["description"] = soup.find_all("div", "description subsection")[0].text
            else:
                print urls[i]
            # provenance = browser.find_element_by_xpath('//p[@class = "headline-1-text created-by"]/following-sibling::*[1]/img')\
            # .get_attribute('alt')
            # coursenames = browser.find_elements_by_xpath('//h2[@class="course-name headline-5-text"]')
            CourseTags = soup.find_all('section', 'rc-Course bgcolor-white')
            for tag in CourseTags:
                id += 1
                course = {}
        
                name = tag.find_all("h2", "course-name headline-5-text")
                if len(name) != 0:
                    course["name"] = name[0].text.decode('utf8').encode('ascii', errors='ignore')
                else:
                    print "no_name", urls[i]

                if len(tag.select('.description-cont')) != 0:
                    course["description"] = tag.select('.description-cont')[0].text
                else:
                    print "no_des", urls[i]
                course["id"] = "coursera" + str(id).zfill(5)
                courseObject["courseSet"].append(course)
            # descriptions = [item.text.encode('ascii','ignore') for item in descriptions]
            # cousenames = [item.text.encode('ascii','ignore') for item in cousenames]
            # coursedic["subject"] = cousenames
        else:
            id += 1
            desc = soup.find_all("p", "body-1-text course-description")
            if len(desc) != 0:
                courseObject["description"] =  soup.find_all("p", "body-1-text course-description")[0].text
            else:
                print urls[i]
            # description = browser.find_element_by_xpath('//p[@class="body-1-text course-description"]')
            courseObject["id"] = "coursera" + str(id).zfill(5)
            # provenance = browser.find_element_by_xpath('//div[@class = "headline-1-text creator-names"]/span[2]')
            # cousename =  browser.find_elements_by_xpath('//h1[@class="title display-3-text"]')
        # description = description.text.encode('ascii','ignore')
    with open('Coursera_web'+ str(j) + '.json', 'a') as f:
        json.dump(page, f)

    content += page
with open('Coursera_web'+ '_content' + '.json', 'a') as f:
    json.dump(content, f)

browser.quit()




