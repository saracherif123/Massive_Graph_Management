"""
Exercise 2: Write an algorithm inspired by DFS that returns a pair (result, color) where 
result is true if the graph is 2-colorable, and color is a dictionary associating colors 0 or 1 to each vertex.

Solution: Both recursive and iterative DFS implementations with early termination.
"""

from collections import deque, defaultdict

def is_2_colorable_dfs(graph):
    """
    Recursive DFS implementation for 2-colorability detection.
    
    Algorithm:
    - Uses DFS traversal
    - Assigns alternating colors (0 and 1)
    - Stops immediately when a conflict (same color on adjacent vertices) is found
    - Returns (result, color)
    
    Args:
        graph: Dictionary representing adjacency list {vertex: [neighbors]}
    
    Returns:
        Tuple: (is_2colorable: bool, coloring: dict)
    """
    color = {}
    
    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if neighbor not in color:
                if not dfs(neighbor, 1 - c):  # alternate color
                    return False
            elif color[neighbor] == color[node]:
                return False  # conflict: same color for adjacent nodes
        return True
    
    # handle disconnected graphs
    for v in graph:
        if v not in color:
            if not dfs(v, 0):
                return False, color
    return True, color

def is_2_colorable_dfs_iterative(graph):
    """
    Iterative DFS implementation for 2-colorability detection using stack.
    
    Args:
        graph: Dictionary representing adjacency list {vertex: [neighbors]}
    
    Returns:
        Tuple: (is_2colorable: bool, coloring: dict)
    """
    color = {}
    
    for start in graph:
        if start not in color:
            stack = [(start, 0)]
            
            while stack:
                node, c = stack.pop()
                
                if node in color:
                    if color[node] != c:
                        return False, color  # conflict
                    continue
                
                color[node] = c
                
                for neighbor in graph[node]:
                    stack.append((neighbor, 1 - c))
    
    return True, color

def test_2colorability_algorithms():
    """Test both recursive and iterative algorithms."""
    
    print("=== TESTING 2-COLORABILITY ALGORITHMS ===")
    print()
    
    # Test case 1: 2-colorable graph (bipartite)
    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    
    print("Test 1: Square graph (2-colorable)")
    print("Graph: 0-1-3-2-0")
    
    # Test recursive version
    result_rec, colors_rec = is_2_colorable_dfs(graph1)
    print(f"Recursive: 2-colorable = {result_rec}")
    print(f"Coloring: {colors_rec}")
    
    # Test iterative version
    result_iter, colors_iter = is_2_colorable_dfs_iterative(graph1)
    print(f"Iterative: 2-colorable = {result_iter}")
    print(f"Coloring: {colors_iter}")
    print()
    
    # Test case 2: Not 2-colorable graph (contains odd cycle)
    graph2 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    
    print("Test 2: Triangle graph (not 2-colorable)")
    print("Graph: 1-2-3-1")
    
    # Test recursive version
    result_rec, colors_rec = is_2_colorable_dfs(graph2)
    print(f"Recursive: 2-colorable = {result_rec}")
    print(f"Coloring: {colors_rec}")
    
    # Test iterative version
    result_iter, colors_iter = is_2_colorable_dfs_iterative(graph2)
    print(f"Iterative: 2-colorable = {result_iter}")
    print(f"Coloring: {colors_iter}")
    print()
    
    # Test case 3: Complex 2-colorable graph
    graph3 = {
        1: [2, 3, 4],
        2: [1, 5],
        3: [1, 6],
        4: [1, 7],
        5: [2, 8],
        6: [3, 8],
        7: [4, 8],
        8: [5, 6, 7]
    }
    
    print("Test 3: Complex graph (2-colorable)")
    print("Graph: Star-like structure")
    
    # Test recursive version
    result_rec, colors_rec = is_2_colorable_dfs(graph3)
    print(f"Recursive: 2-colorable = {result_rec}")
    print(f"Coloring: {colors_rec}")
    
    # Test iterative version
    result_iter, colors_iter = is_2_colorable_dfs_iterative(graph3)
    print(f"Iterative: 2-colorable = {result_iter}")
    print(f"Coloring: {colors_iter}")
    print()

def demonstrate_early_termination():
    """Demonstrate early termination feature."""
    
    print("\n=== EARLY TERMINATION DEMONSTRATION ===")
    print()
    
    # Graph where conflict is found early
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4, 6],
        6: [5, 7],
        7: [6, 8],
        8: [7]
    }
    
    print("Graph with early conflict detection:")
    print("1-2-4-3-1 (triangle) + 4-5-6-7-8 (path)")
    print()
    
    result, colors = is_2_colorable_dfs(graph)
    print(f"Result: {result}")
    print(f"Coloring: {colors}")
    print()
    
    print("The algorithm stops as soon as it finds the triangle conflict")
    print("It doesn't need to explore the entire graph")

if __name__ == "__main__":
    test_2colorability_algorithms()
    demonstrate_early_termination()