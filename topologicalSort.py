# implementing top sort from scratch, using edges
# assuming there are no cyclic graphs present
# find node(s) with no incoming edges add them to list
# graph data structure to allow easy removing

# dict = {node: [[outgoing], [incoming]]}

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
    cur = []
    return cur


edges = [[1,0],[2,0],[3,1],[3,2]]
graph = parse(edges)
print(topsort(graph))
