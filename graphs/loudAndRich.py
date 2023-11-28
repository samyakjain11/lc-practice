
import collections
from typing import *
import treeViz

def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    # answer[i] = loudest person who is richer than i
    # create DAG for richness
    # index graph like so: map[i] = [list of poeple richer than them]
    richGraph = collections.defaultdict(list)
    for richerPerson, poorerPerson in richer:
        richGraph[poorerPerson].append(richerPerson)
    
    # treeViz.graphIt(richGraph)
    
    print(richGraph)
    def gatherAllRicher(node):
        curRicher = richGraph[node].copy()
        stack = richGraph[node].copy()
        while stack:
            cur = stack.pop()
            stack += richGraph[cur]
            curRicher += richGraph[cur]
        return curRicher
    
    answer = []
    for i in range(len(quiet)):
        moreRich = gatherAllRicher(i)
        moreRich.append(i)
        print(moreRich)
        quietList = [(quiet[j-1], j) for j in moreRich]
        quietList.sort(reverse=True)
        answer.append(quietList[0][1])
    return answer


richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
loudAndRich(richer, quiet)