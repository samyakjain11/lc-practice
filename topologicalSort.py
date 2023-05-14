# implementing top sort from scratch, using edges
# assuming there are no cyclic graphs present- edit no need, enforce a simple check prior
# find node(s) with no incoming edges add them to list
# graph data structure to allow easy removing

# dict = {node: [[outgoing], [incoming]]}

from typing import Dict

def parse(edges):
    graph = {}
    existing_nodes = set()
    for edge in edges:
        out, inc = edge
        if out not in existing_nodes:
            existing_nodes.add(out)    
            graph[out] = [[],[]]
        if inc not in existing_nodes:
            existing_nodes.add(inc)
            graph[inc] = [[],[]]
        # out and inc exist inside the graph just as nodes with no links
        # add links!
        graph[out][0].append(inc)
        graph[inc][1].append(out)
    return graph
    


def topsort(graph):
    # find nodes with no incoming edges
    # add them to cur
    # remove those nodes from the graph
    # recursively call topsort for cur = (no incoming edges nodes) + (recursive call result)
    # add another check to see if there are no nodes without any incoming edges then the graph is cyclic!!
    if len(graph) == 0:
        return []
    cur = []
    cyclic = True
    for node in list(graph.keys()):
        if len(graph[node][1]) == 0: # length of incoming edges to this node
            cyclic = False
            cur.append(node)
    if cyclic:
        print(graph)
        return False
    
    for node in cur:
        # remove edges
        outgoing_edges = graph[node][0]
        for outgoing in outgoing_edges:
            graph[outgoing][1].remove(node)
        # remove from graph
        graph.pop(node)
    
    # recursive call
    ret = topsort(graph)
    if ret == False:
        return False
    else:
        return cur + ret 


edges = [[1,0],[2,0],[3,1],[3,2]]
graph = parse(edges)
# topsort(graph)
print(topsort(graph))
# graph = {}
# print(len(graph))
# graph[1] = 0
# graph.pop(1)
# print(graph)