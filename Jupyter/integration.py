from py2neo import Graph,NodeSelector
import neo
from ipywidgets import *
from IPython.display import display, HTML
neo.init_notebook_mode() 
graph = Graph("http://localhost:7474/db/data/")

searchbox = widgets.Text(
        placeholder='Prgram Name',
        description='Search:',
        disabled=False)

def program_result(plist):
    items_layout = Layout(
        flex='1 1 auto',
        width='auto')     # override the default width of the button to 'auto' to let the button grow

    box_layout = Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='60%')
    items = [ToggleButton(description=w, layout=items_layout) for w in plist]
    return Box(children=items, layout=box_layout)

def search_program(keyword):
    query = "MATCH (p:Program) WHERE p.name =~ '(?i).*"+keyword+".*' RETURN p LIMIT 10"
    data = graph.data(query)
    return [p['p']['name'] for p in data]

def value_changed(change):
    res = search_program(change.new)
    box = program_result(res)
    display(box)
    value_changed.box = box.children

searchbox.observe(value_changed, 'value')

display(searchbox)

button = widgets.Button(description="See Detail!")

def on_button_clicked(b):
    for box in value_changed.box:
        if box.value == True:
            selected = box.description
    visualize(selected)

button.on_click(on_button_clicked)
display(button)

def refernce_display(clist):
    content = '''
        <table style="width:100%" bordercolor='lightgreen'>
          <tr>
            <th style="text-align:left"; width="10%;">Code</th>
            <th style="text-align:left"; width="30%;">Name</th> 
            <th style="text-align:left"; width="20%;">Image</th>
            <th style="text-align:left"; width="40%;">MOOC</th>
          </tr>
          '''
    for c in clist:
        content += '''
            <tr>
                <td style="text-align:left";>''' + c['code'] + '''</td>
                <td style="text-align:left";>''' + c['name'] + '''</td> 
                <td><img src=''' + c['image'] + ''' height="120px"; display: inline-block;></td>
                <td style="text-align:left";> <a href="''' + c['url'] + '''" target="_blank">''' + c['mooc'] + '''</td></tr>'''
    #return content
    display(HTML(content))


from collections import defaultdict
from py2neo import Graph
import pandas as pd


def TopoSort(program_name):
    graph = Graph("http://localhost:7474/db/data/")
    adjPair = graph.data("MATCH (m)-[:HasPrerequisite]->(n) \
        WHERE (m)-[:UnderProgram]->({name:" + program_name + "}) \
        and (n)-[:UnderProgram]->({name:" + program_name + "}) \
        RETURN m.id, n.id")

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

    courselist = []
    for i in adjPair:
        courselist += [i["m.id"], i["n.id"]]
    courselist = list(set(courselist))

    g = Prerequisite(courselist)
    for edge in adjPair:
        g.addEdge(edge["m.id"], edge["n.id"])
    # MATCH (n:Course{id:"BUAD 280"}) RETURN n
    toposort = g.tps()

    
    nodes = []
    course = list()
    relation = list()
    relat = []
    import pandas as pd
    for id in toposort[::-1]:
        dic = {}
        node = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n")
        coursename = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n.name")[0]
        coursedesc = graph.data("Match (n:Course{id:'" + id + "'}) RETURN n.description")[0]
        mooc = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.name limit 1")
        image = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.image limit 1")
        url = graph.data("MATCH p = (n:Course{id:'"+ id + "'})-[r:SimilarTo]->(m:MOOC) RETURN m.url limit 1")
        print(mooc)
        dic["code"] = id
        dic["name"] = coursename["n.name"]
        dic["mooc"] = ""
        dic["url"] = ""
        dic["image"] = ""
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

    import json
    j = json.dumps(relat)
 
