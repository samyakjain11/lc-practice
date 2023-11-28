# import pydot

# def graphIt(menu):
#     def stringParse(menu):
#         newMenu = {}
#         for key in menu.keys():
#             newMenu[str(key)] = [str(value) for value in menu[key]]
#         return newMenu

#     def draw(parent_name, child_name):
#         edge = pydot.Edge(parent_name, child_name)
#         graph.add_edge(edge)
        
#     def visit(node, parent=None):
#         for k,v in node.items():# If using python3, use node.items() instead of node.iteritems()
#             if isinstance(v, dict):
#                 # We start with the root node whose parent is None
#                 # we don't want to graph the None node
#                 if parent:
#                     draw(parent, k)
#                 visit(v, k)
#             else:
#                 draw(parent, k)
#                 # drawing the label using a distinct name
#                 draw(k, k+'_'+v)

#     ourNewMenu = stringParse(menu)
#     graph = pydot.Dot(graph_type='graph')
#     visit(ourNewMenu)
#     graph.write_png('example1_graph.png')