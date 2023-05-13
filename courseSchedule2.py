from collections import deque
from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initialize the graph as adjacency list
        source_nodes = set()
        graph = defaultdict(list)
        # graph = {}
        for edge in prerequisites:
            source_nodes.add(edge[0])
            if edge[1] in source_nodes:
                source_nodes.remove(edge[1])

            graph[edge[0]] += [edge[1]]
            graph[[edge[1]]] = []

        
        # this means there is a course that you can not get to
        if numCourses != len(list(graph.keys())): 
            return []
        
        # check for cycles
        rets = {}
        def dfs(stack, seen):
            top = stack.pop()
            if top in seen:
                return False
            for neighbor in graph[top]:
                copy_seen, copy_stack = seen.copy(), stack.copy()
                copy_seen.add(neighbor); copy_stack.append(neighbor)
                ret = dfs(copy_stack, copy_seen)
                del copy_seen, copy_stack
                if ret == True:
                    rets[top] = True
                else:
                    return False
            
            # at this point the dfs suceeded so true
            return True
        

        for starting_node in source_nodes:
            res = dfs([starting_node], set())
            if res == False:
                return []
            
        # now we know there are no cycles so we can proceed to implement top sort
        
        



        

