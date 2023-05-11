from collections import deque
# Definition for a Node.
from typing import List
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.marked = False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph, perform dfs, check for cycles
        if len(prerequisites) == 0:
            return True


        source_nodes = set()
        nodes = {} # map value to node
        for tup in prerequisites:
            source_val, sink_val = tup
            if source_val == sink_val:
                return False
            if sink_val not in nodes.keys():
                sink_node = Node(sink_val)
                nodes[sink_val] = sink_node
            if source_val not in nodes.keys():
                source_node = Node(source_val)
                nodes[source_val] = source_node
            
            source_node = nodes[source_val]
            sink_node = nodes[sink_val]
            
            source_node.neighbors.append(sink_node)
            source_nodes.add(source_node)
            if sink_node in source_nodes:
                source_nodes.remove(sink_node) 

        # print([source_node.val for source_node in source_nodes])
        if len(source_nodes) == 0:
            return False
        else:
            # mf dfs
            rets = {}
            def dfs(stack):
                top = stack.pop()
                if top in rets.keys():
                    return True
                if top.marked:
                    # print(f'returning bc {top.val} has been visited')
                    return False
                top.marked = True
                for n in top.neighbors:
                    # print(f'starting {top.val} nested {n.val}')
                    stack.append(n)
                    if not dfs(stack.copy()):
                        # print(f'returning bc dfs({n.val}) returned false')
                        return False
                    stack.remove(n)
                top.marked = False
                
                rets[top] = True
                return True
            
            for source in list(source_nodes):
                print('starting root path')
                source.marked = False
                dfs_ret = dfs([source])
                source.marked = False
                if not dfs_ret:
                    return False
            return True
                
                
            
                



                


            


            
