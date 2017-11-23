import json 

# coursera = json.load(open('Coursera_data.json'))

# csr = []
# spe_id = 0
# for item in coursera:
#     if unicode("courseSet") in item:
#         spe_id += 1
#         item["special_id"] = "spc" + str(spe_id).zfill(5)
#         list = item[unicode("courseSet")]
#         clist = []
#         for course in list:
#             c = {}
#             original = course[unicode("id")] 
#             c["id"] = "csr" + original[-5:]
#             c["course_name"] = course[unicode("name")]
#             clist.append(c["id"])
#         item[unicode("courseList")] = clist
#         del item[unicode("courseSet")]
#         del item[unicode("specialization")]
#         del item[unicode("description")]
#         del item[unicode("course_url")]
#         del item[unicode("img")]
#         # if unicode("description") in item:
#         #     s = item[unicode("description")]
#         #     item["description"] = Format_desc(s)
#         # else:
#         #     item["description"] = "Empty"
#         csr.append(item)

# print len(csr)
# with open("Specialization.json", "a") as f:
#     json.dump(csr, f)

coursera = json.load(open('Coursera_data.json'))

csr = []
spe_id = 0
duplicate = []
for item in coursera:
    if unicode("courseSet") in item and item["name"] not in duplicate:
        spe_id += 1
        item["special_id"] = "spc" + str(spe_id).zfill(5)
        list = item[unicode("courseSet")]
        clist = []
        for course in list:
            c = {}
            original = course[unicode("id")] 
            c["id"] = "csr" + original[-5:]
            c["course_name"] = course[unicode("name")]
            clist.append(c["id"])
        item[unicode("courseList")] = ', '.join(clist)
        del item[unicode("courseSet")]
        del item[unicode("specialization")]
        del item[unicode("description")]
        del item[unicode("course_url")]
        del item[unicode("img")]
        csr.append(item)
        duplicate.append(item["name"])

print len(csr)
with open("Specialization3.json", "a") as f:
    json.dump(csr, f)
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_json("Specialization3.json")
# print(df)
df.to_csv('Specialization2.csv')




