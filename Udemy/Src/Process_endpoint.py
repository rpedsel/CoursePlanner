import json


data = json.load(open('udacity_endpoint.json'))
print len(data["courses"])

courselist = []
i = 0
for object in data["courses"]:
    i += 1
    course_obj = {}
    course_obj["id"] = "udacity" + str(i).zfill(5)
    course_obj["name"] = object["title"]
    course_obj["course_url"] = object["homepage"]
    if len(object["affiliates"]) != 0:
        course_obj["provenance"] = object["affiliates"]
    else:
        course_obj["provenance"] = [{"name": "udacity"}]
    course_obj["description"] = object["expected_learning"] + ' ' + object["summary"]
    courselist.append(course_obj)

with open('udacity_data.json', 'a') as f:
    json.dump(courselist, f)

# print courselist

# print data["courses"][0]