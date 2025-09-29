"""
Exercise 3: Propose an algorithm that determines if a graph contains an odd cycle.

Solution: Use BFS with vertex coloring to detect odd cycles.
If we find a back edge that connects two vertices of the same color, 
we have found an odd cycle.
"""

from collections import deque, defaultdict

def has_odd_cycle(graph):
    """
    Determine if a graph contains an odd cycle using BFS with vertex coloring.
    
    Algorithm: Use BFS with coloring - color neighbors alternately.
    If a neighbor is already colored with the same color, an odd cycle exists.
    
    Args:
        graph: Dictionary representing adjacency list {vertex: [neighbors]}
    
    Returns:
        Boolean: True if graph contains an odd cycle, False otherwise
    """
    # A dictionary to store the "color" (0 or 1) assigned to each vertex.
    # Empty at the start → no node is colored.
    color = {}
    
    # We loop through all nodes (important for disconnected graphs).
    for node in graph:
        # If a node hasn't been colored yet, we start BFS from it.
        if node not in color:
            queue = deque([node])
            # Assign it color 0 and push into the queue.
            color[node] = 0
            
            # BFS traversal:
            while queue:
                u = queue.popleft()
                # For every neighbor v of u:
                for v in graph[u]:
                    # If v has no color yet, assign the opposite color to u (so 0 → 1, or 1 → 0).
                    if v not in color:
                        color[v] = 1 - color[u]   # assign opposite color
                        queue.append(v)
                    # If v already has the same color as u, then the graph is not bipartite 
                    # → it must contain an odd cycle → return True.
                    elif color[v] == color[u]:
                        return True  # odd cycle found
    
    # After exploring the whole graph (all components), if no conflict was found → no odd cycle.
    # If BFS finishes without conflicts, no odd cycle was found.
    return False

def test_odd_cycle_detection():
    """Test the odd cycle detection algorithm."""
    
    print("=== TESTING ODD CYCLE DETECTION ===")
    print()
    
    # Test case 1: Graph with odd cycle (triangle)
    graph1 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    
    print("Test 1: Triangle (odd cycle)")
    print("Graph: 1-2-3-1")
    print(f"Has odd cycle: {has_odd_cycle(graph1)}")
    if has_odd_cycle(graph1):
        print("→ Graph is NOT bipartite")
    else:
        print("→ Graph IS bipartite")
    print()
    print()
    
    # Test case 2: Graph with even cycle (square)
    graph2 = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3]
    }
    
    print("Test 2: Square (even cycle)")
    print("Graph: 1-2-3-4-1")
    print(f"Has odd cycle: {has_odd_cycle(graph2)}")
    if has_odd_cycle(graph2):
        print("→ Graph is NOT bipartite")
    else:
        print("→ Graph IS bipartite")
    print()   
    print()
    
    # Test case 3: Complex graph
    graph3 = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4, 5],
        4: [2, 3, 6],
        5: [3, 6],
        6: [4, 5]
    }
    
    print("Test 3: Complex graph")
    print("Graph with multiple cycles")
    print(f"Has odd cycle: {has_odd_cycle(graph3)}")
    if has_odd_cycle(graph3):
        print("→ Graph is NOT bipartite")
    else:
        print("→ Graph IS bipartite")
    print()
    print()
    
    # Test case 4: Test graph from Exercise 5
    graph_test = {
        0: [1, 5],
        1: [0, 2, 5],
        2: [1, 3, 4],
        3: [2, 4],
        4: [2, 3, 5],
        5: [0, 1, 4]
    }
    
    print("Test 4: Exercise 5 test graph")
    print("Graph: 0-1-2-3-4-5-0")
    print(f"Graph has odd cycle: {has_odd_cycle(graph_test)}")
    if has_odd_cycle(graph_test):
        print("→ Graph is NOT bipartite")
    else:
        print("→ Graph IS bipartite")
    print()

if __name__ == "__main__":
    test_odd_cycle_detection()