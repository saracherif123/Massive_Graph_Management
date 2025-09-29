"""
Exercise 1: Using graph traversal algorithms, propose an algorithm that computes 
the number of edges between a given vertex and all other vertices.

Solution: Use Breadth-First Search (BFS) to compute shortest distances.
Following the exact pseudocode with FIFO queue data structure.
"""

from collections import deque, defaultdict

class Queue:
    """
    Queue data structure implementing FIFO (First In First Out).
    Elements first added are first removed.
    """
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self.items)

def bfs_exact_pseudocode(graph, start_vertex):
    """
    BFS implementation following the exact pseudocode provided.
    
    Pseudocode:
    1: procedure BFS(G(V, E), r)
    2: Q ← ∅, enqueue(Q, r)
    3: r.label = true
    4: while Q ≠ ∅ do
    5: v ← dequeue(Q)
    6: for w ∈ Nv do
    7: if ¬w.label then
    8: enqueue(Q, w)
    9: w.label = true
    10: end if
    11: end for
    12: end while
    13: end procedure
    
    Args:
        graph: Dictionary representing adjacency list {vertex: [neighbors]}
        start_vertex: The starting vertex
    
    Returns:
        Dictionary mapping each vertex to its visited status
    """
    # Initialize labels (visited status) for all vertices
    labels = {}
    for vertex in graph:
        labels[vertex] = False
    
    # Step 2: Q ← ∅, enqueue(Q, r)
    Q = Queue()
    Q.enqueue(start_vertex)
    
    # Step 3: r.label = true
    labels[start_vertex] = True
    
    # Step 4: while Q ≠ ∅ do
    while not Q.is_empty():
        # Step 5: v ← dequeue(Q)
        v = Q.dequeue()
        
        # Step 6: for w ∈ Nv do
        for w in graph[v]:
            # Step 7: if ¬w.label then
            if not labels[w]:
                # Step 8: enqueue(Q, w)
                Q.enqueue(w)
                # Step 9: w.label = true
                labels[w] = True
    
    return labels

def compute_distances_from_vertex(graph, start_vertex):
    """
    Compute the number of edges (shortest path) between a given vertex and all other vertices.
    Enhanced version that computes distances while following BFS principles.
    
    Args:
        graph: Dictionary representing adjacency list {vertex: [neighbors]}
        start_vertex: The starting vertex
    
    Returns:
        Dictionary mapping each vertex to its distance from start_vertex
    """
    # Initialize distances dictionary
    distances = {}
    labels = {}
    
    # Initialize all distances to infinity (unvisited) and labels to False
    for vertex in graph:
        distances[vertex] = float('inf')
        labels[vertex] = False
    
    # Distance from start_vertex to itself is 0
    distances[start_vertex] = 0
    
    # BFS queue using FIFO principle
    Q = Queue()
    Q.enqueue(start_vertex)
    labels[start_vertex] = True
    
    while not Q.is_empty():
        v = Q.dequeue()
        
        # Visit all neighbors of current vertex
        for w in graph[v]:
            if not labels[w]:
                Q.enqueue(w)
                labels[w] = True
                distances[w] = distances[v] + 1
    
    return distances

def print_distances(distances, start_vertex):
    """Helper function to print the results in a readable format."""
    print(f"Distances from vertex {start_vertex}:")
    for vertex, distance in sorted(distances.items()):
        if distance == float('inf'):
            print(f"  {vertex}: unreachable")
        else:
            print(f"  {vertex}: {distance} edges")

def demonstrate_queue_fifo():
    """Demonstrate FIFO behavior of the queue."""
    print("=== QUEUE FIFO DEMONSTRATION ===")
    print()
    
    Q = Queue()
    print("Enqueueing elements: 1, 2, 3, 4, 5")
    for i in [1, 2, 3, 4, 5]:
        Q.enqueue(i)
        print(f"Enqueued {i}, Queue: {Q.items}")
    
    print("\nDequeueing elements (FIFO - First In First Out):")
    while not Q.is_empty():
        item = Q.dequeue()
        print(f"Dequeued {item}, Queue: {Q.items}")
    print()

def test_bfs_algorithms():
    """Test both BFS implementations."""
    print("=== TESTING BFS ALGORITHMS ===")
    print()
    
    # Example graph: undirected graph
    #    1---2---3
    #    |   |   |
    #    4---5---6
    example_graph = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5],
        5: [2, 4, 6],
        6: [3, 5]
    }
    
    print("Example graph:")
    print("    1---2---3")
    print("    |   |   |")
    print("    4---5---6")
    print()
    
    start_vertex = 1
    
    # Test exact pseudocode implementation
    print("1. BFS following exact pseudocode:")
    labels = bfs_exact_pseudocode(example_graph, start_vertex)
    print(f"Visited vertices from {start_vertex}: {[v for v, visited in labels.items() if visited]}")
    print()
    
    # Test distance computation
    print("2. BFS with distance computation:")
    distances = compute_distances_from_vertex(example_graph, start_vertex)
    print_distances(distances, start_vertex)
    print()
    
    # Test with different starting vertices
    print("3. Testing with different starting vertices:")
    for start in [2, 5]:
        distances = compute_distances_from_vertex(example_graph, start)
        print_distances(distances, start)
        print()

# Example usage
if __name__ == "__main__":
    demonstrate_queue_fifo()
    test_bfs_algorithms()

