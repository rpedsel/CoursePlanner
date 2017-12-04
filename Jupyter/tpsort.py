import json, jgraph
import pandas as pd
from py2neo import Graph
from collections import defaultdict


class Prerequisite:
    def __init__(self, courselist):
        self.graph = defaultdict(list) 
        self.vertices = courselist
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def dfs(self, v, visit, order):
        visit[v] = True
        for u in self.graph[v]:
            if visit[u] == False:
                self.dfs(u, visit, order)
        order.insert(0, v)
 
    def tps(self):
        visit = {v: False for v in self.vertices}
        order =[]
        for v in self.vertices:
            if visit[v] == False:
                self.dfs(v, visit, order)
        return order


def topo_Sort(program_name):
    graph = Graph("http://localhost:7474/db/data/")
    adjPair = graph.data("MATCH (m)-[:HasPrerequisite]->(n) \
        WHERE (m)-[:UnderProgram]->({name:" + program_name + "}) \
        and (n)-[:UnderProgram]->({name:" + program_name + "}) \
        RETURN m.id, n.id")

    courselist = []
    for i in adjPair:
        courselist += [i["m.id"], i["n.id"]]
    courselist = list(set(courselist))

    g = Prerequisite(courselist)
    for edge in adjPair:
        g.addEdge(edge["m.id"], edge["n.id"])
    # MATCH (n:Course{id:"BUAD 280"}) RETURN n
    toposort = g.tps()
    return toposort[::-1]


def display_list(order):
    nodes, relat = [], []
    course, relation = list(), list()

    for id in order:
        dic = {}
        dic["code"], dic["mooc"], dic["url"], dic["image"] = id, "", "", ""
        node = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n")
        coursename = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n.name")[0]
        coursedesc = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n.description")[0]
        mooc = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.name limit 1")
        image = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.image limit 1")
        url = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.url limit 1")
        dic["name"] = coursename["n.name"]
        if len(mooc) != 0:
            rlist = [id, coursename["n.name"], mooc[0]["m.name"], image[0]["m.image"], url[0]["m.url"]]
            relation.append(rlist)
            dic["mooc"], dic["image"], dic["url"] = rlist[2], rlist[3], rlist[4]
        relat.append(dic)
        nodes += node
        course.append([id, coursename["n.name"], coursedesc["n.description"]])
    course_df = pd.DataFrame(course)
    relation_df = pd.DataFrame(relation)
    # relat
    relation_df
    refernce_display(relat)
    j = json.dumps(relat)
