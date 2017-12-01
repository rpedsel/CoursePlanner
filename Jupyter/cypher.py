from py2neo import Graph
graph = Graph("http://localhost:7474/db/data/")
# remove self loop
graph.data("match (n)-[r]->(n) delete r")
# return graph
graph.data("MATCH p = ()-[r:UnderProgram]->(n {name: program_name}) RETURN p")
# match (n)-[r:HasDuplicate]->(n) delete r
# MATCH (n {name: 'Alice'})->(m)
# "Accounting (BS)"
MATCH p = ()-[r: UnderProgram]->(n {name: "Accounting (BS)"}) RETURN p

MATCH (m)-[r:UnderProgram]->(n {name: 'Accounting (BS)'})
where (m)-[r:HasPreparation]->()


graph_3.data("MATCH (m)-[r:UnderProgram]->(n {name: 'Accounting (BS)'})\
where not (m)-[r:HasPreparation]->() and not (m)-[r:HasPrerequisite]->()\
return m")



MATCH (k)-[r*]->(n:ABC)
with k, r, n, count(k)

import pandas as pd
courses = list()
courselist = graph_3.data("MATCH p = (m)-[r:UnderProgram]->(n {name: 'Accounting (BS)'}) return p")
for course in courselist:
    graph_3.data("Match ")
