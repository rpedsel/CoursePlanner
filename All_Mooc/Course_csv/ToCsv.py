import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_json("Coursera_flat.json")
print(df)
df.to_csv('Coursera_flat.csv')

df = pd.read_json("Catalogue_course.json")
print(df)
df.to_csv('Catalogue_course.csv')

df = pd.read_json("Mooc_merge.json")
print(df)
df.to_csv('Mooc_merge.csv')
values = json.load(open("Catalogue_course.json"))
import csv
with open("Catalogue_course.csv", "wb") as f:
    wr = csv.writer(f)
    for data in values:
         for key, value in data.iteritems():
               wr.writerow([",".join([v.encode("utf-8") for v in value]) if isinstance(value, list) else value.encode("utf8")])
