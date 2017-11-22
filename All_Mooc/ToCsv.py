import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_json("Coursera_flat.json")
print(df)
df.to_csv('Coursera_flat.csv')

df = pd.read_json("Catalogue.json")
print(df)
df.to_csv('Catalogue.csv')

df = pd.read_json("Mooc_merge.json")
print(df)
df.to_csv('Mooc_merge.csv')
