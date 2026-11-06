"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #U: Return deep copy of the graph (input == output)

        #M/P: 
            # DFS
            # Initialize hashmap (oldToNew)
            # Create an inner dfs function 
                # If node is already in hashmap, return the copy/sublist of neighbors for that node 

                # Create copy of node 
                # Add node and corresponding copy to hashmap (node is the key, copy is the value)
                
                # Iterate through the neighbors of each node with for loop
                    # Add new nodes to copy (acts as the sublist): copy.neighbors.append(dfs(neighbor))
                
                # Return copy (sublist of neighbors for each node)
                
            # Return dfs(node)

        #I: 
        oldToNew = {} 

        def dfs(node):
            if not node: 
                return None 
                 
            if node in oldToNew: 
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy #Creates clone of the node 

            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor)) 

            return copy 

        return dfs(node)
        