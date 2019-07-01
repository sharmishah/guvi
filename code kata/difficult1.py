def isTree(self): 
        # Mark all the vertices as not visited  
        # and not part of recursion stack 
        visited = [False] * self.V 
  
        # The call to isCyclicUtil serves multiple  
        # purposes. It returns true if graph reachable  
        # from vertex 0 is cyclcic. It also marks  
        # all vertices reachable from 0. 
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False
  
        # If we find a vertex which is not reachable 
        # from 0 (not marked by isCyclicUtil(),  
        # then we return false 
        for i in range(self.V): 
            if visited[i] == False: 
                return False
  
        return True
  
# Driver program to test above functions 
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 
print "Graph is a Tree" if g1.isTree() == True \ 
                          else "Graph is a not a Tree"
  
g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 
print "Graph is a Tree" if g2.isTree() == True \ 
                          else "Graph is a not a Tree"
