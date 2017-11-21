import json 
 
# with open('Coursera_data.json', 'r') as f:
#     json.load()

coursera = json.load(open('Coursera_data.json'))
edX = json.load(open('edX.json'))
khan = json.load(open('khan_data.json'))
udacity = json.load(open('udacity_data.json'))
print len(coursera), len(edX), len(khan), len(udacity)

# id in 3 digits letter + 5 digits number
# remove unicode, starting words
def Format_desc(s):
    # s = item[unicode("description")]
    # s = s.replace("About this course: ", "")
    # s = s.replace("About the Course", "")
    Useless = ["About the Course", "about this course ", \
    "About this Course\n\n", "This course",\
    "About this course: ", "In this course",\
    "in this course", "this course", "Welcome to "\
    "\n\n", " \n", "   \n\n", "\n\t", "This is a course",\
    "In this course,", "in this course,", "About the course"]
    # s = s.replace("In this course", "")
    # s = s.replace("in this course", "")
    for ul in Useless:
        s = s.replace(ul, "")
    s = s.encode('ascii','ignore')
    s = s.encode('ascii','replace')
    return s.strip()


csr = []
spe_id = 0
for item in coursera:
    # if unicode("provenance") not in item:
    #     print item
    # else:
    #     print item[unicode("provenance")]
    if unicode("courseSet") in item:
    # if len(item[unicode("courseSet")]) > 1:
        del item[unicode("description")]
        spe_id += 1
        list = item[unicode("courseSet")]
        for course in list:
            course["img"] = item[unicode("img")]
            if unicode("provenance") in item:
                course["provenance"] = item[unicode("provenance")]
            else:
                course["provenance"] = "cousera"
            course[unicode("course_url")] = item[unicode("course_url")]
            course[unicode("special_id")] = "spc" + str(spe_id).zfill(5)
            original = course[unicode("id")] 
            course["id"] = "csr" + original[-5:]
            s = course[unicode("description")]
            # s = s.replace("About this course: ", "")
            # s = s.replace("About the Course", "")
            del course[unicode("description")]
            course["description"] = Format_desc(s)
            csr.append(course)
    else:
        original = item[unicode("id")] 
        item[unicode("id")] = "csr" + original[-5:]
        if unicode("description") in item:
            s = item[unicode("description")]
            # s = s.replace("About this course: ", "")
            # s = s.replace("About the Course", "")
            # s = s.replace("In this course", "")
            # s = s.replace("in this course", "")
            # s = s.encode('ascii','ignore')
            # a.encode('ascii','replace')
            item["description"] = Format_desc(s)
        else:
            item["description"] = "Empty"
        del item["specialization"]
        csr.append(item)

print len(csr)
with open("Coursera_flat.json", "a") as f:
    json.dump(csr, f)


khn = []
for item in khan:
    original = item[unicode("id")] 
    item[unicode("id")] = "khn" + original[-5:]
    if unicode("description") in item:
        s = item[unicode("description")]
        item["description"] = Format_desc(s)
    else:
        item["description"] = "Empty"
    khn.append(item)

udc = []
for item in udacity:
    original = item[unicode("id")] 
    item[unicode("id")] = "udc" + original[-5:]
    if unicode("description") in item:
        s = item[unicode("description")]
        item["description"] = Format_desc(s)
    else:
        item["description"] = "Empty"
    udc.append(item)
print len(udc), len(khn)

Mooc_merge = csr + edX + khn + udc
print len(Mooc_merge)

with open("Mooc_merge.json", "a") as f:
    json.dump(Mooc_merge, f)





