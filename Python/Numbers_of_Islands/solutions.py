from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Convert it to a legit graph
        m, n = len(grid), len(grid[0])
        Graph = {}
        for II in range(m): 
            for JJ in range(n): 
                if grid[II][JJ] == "1":
                    Graph[II, JJ] = []
                    for Neighbour in [(II - 1, JJ), (II, JJ - 1), (II + 1, JJ), (II, JJ + 1)]: 
                        if  Neighbour[0] >= 0 and Neighbour[0] < m and \
                            Neighbour[1] >= 0 and Neighbour[1] < n and grid[II][JJ] == "1": 
                            Graph[II, JJ].append(Neighbour)
        print(Graph)
        Counter = 0
        Unvisited = set(Graph.keys())
        while len(Unvisited) != 0:
            Queue = [next(iter(Unvisited))]
            while len(Queue) != 0:
                Node = Queue.pop(0)
                if Node not in Unvisited: # visited can be repeated in the queue. 
                    continue 
                Unvisited.remove(Node)
                for Neighbour in Graph[Node]:
                    if Neighbour in Unvisited:
                        Queue.append(Neighbour) 
            Counter += 1
        return Counter
            
            
                        
        
