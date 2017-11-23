import json 
import pandas as pd
catalogue = json.load(open("Catalogue_sim.json"))
inter_link = []

# for course in catalogue:
#     if len(course["prerequisite"]) > 0 or len(course["preparation"]) > 0\
#     or len(course["corequisite"]) > 0 or len(course["duplicate"]) > 0\
#     or  len(course["crosslist"]) > 0:
#         del course["description"]

#         if len(course["prerequisite"]) >= 1:
#             se1 = course["prerequisite"]
#             course["prerequisite"] = [i.encode('UTF8') for i in dict.fromkeys(se1).keys()]

#         if len(course["preparation"]) >= 1:
#             se2 = course["preparation"]
#             course["preparation"] = [i.encode('UTF8') for i in dict.fromkeys(se2).keys()]

#         if len(course["corequisite"]) >= 1:
#             se3 = course["corequisite"]
#             course["corequisite"] = [i.encode('UTF8') for i in dict.fromkeys(se3).keys()]

#         if len(course["duplicate"]) >= 1:
#             se4 = course["duplicate"]
#             course["duplicate"] = [i.encode('UTF8') for i in dict.fromkeys(se4).keys()]

#         if len(course["crosslist"]) >= 1:
#             se5 = course["crosslist"]
#             course["crosslist"] = [i.encode('UTF8') for i in dict.fromkeys(se5).keys()]

#         empty = []
#         for key in course:
#             if len(course[key]) == 0:
#                 empty.append(key)
#             # if len(course[key]) == 1:
#             #     course[key] = course[key][0]
#         if len(course["similarity"]) != 0:
#             course["similar_mooc"] = []
#             for item in course["similarity"]:
#                 course["similar_mooc"] += [item[0]]
#             print course["similar_mooc"]
#             list = course["similar_mooc"]
#             course["similar_mooc"] = ', '.join([i.encode('UTF8') for i in list])
#             del course["similarity"]
#         for key in empty:
#             del course[key]
#         inter_link.append(course)

# print len(inter_link)
# # print inter_link
# with open("inter_link0.json", "a") as f:
#     json.dump(inter_link, f)




for course in catalogue:
    if len(course["prerequisite"]) > 0 or len(course["preparation"]) > 0\
    or len(course["corequisite"]) > 0 or len(course["duplicate"]) > 0\
    or  len(course["crosslist"]) > 0:
        del course["description"]

        if len(course["prerequisite"]) > 1:
            se1 = course["prerequisite"]
            course["prerequisite"] = ', '.join([i.encode('UTF8') for i in dict.fromkeys(se1).keys()])

        if len(course["preparation"]) > 1:
            se2 = course["preparation"]
            course["preparation"] = ', '.join([i.encode('UTF8') for i in dict.fromkeys(se2).keys()])

        if len(course["corequisite"]) > 1:
            se3 = course["corequisite"]
            course["corequisite"] = ', '.join([i.encode('UTF8') for i in dict.fromkeys(se3).keys()])

        if len(course["duplicate"]) > 1:
            se4 = course["duplicate"]
            course["duplicate"] = ', '.join([i.encode('UTF8') for i in dict.fromkeys(se4).keys()])

        if len(course["crosslist"]) > 1:
            se5 = course["crosslist"]
            course["crosslist"] = ', '.join([i.encode('UTF8') for i in dict.fromkeys(se5).keys()])

        empty = []
        for key in course:
            if len(course[key]) == 0:
                empty.append(key)
        if len(course["similarity"]) != 0:
            course["similar_mooc"] = []
            for item in course["similarity"]:
                course["similar_mooc"] += [item[0]]
            print course["similar_mooc"]
            list = course["similar_mooc"]
            course["similar_mooc"] = ', '.join([i.encode('UTF8') for i in list])
            del course["similarity"]
        for key in empty:
            del course[key]
        inter_link.append(course)
        
for course in inter_link:
    for key in course:
        if len(course[key]) == 1:
            course[key] = course[key][0]

print len(inter_link)
# print inter_link
with open("inter_link.json", "a") as f:
    json.dump(inter_link, f)
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_json("inter_link.json")
# print(df)
df.to_csv('inter_link.csv')
