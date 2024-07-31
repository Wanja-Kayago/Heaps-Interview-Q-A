MinHeap Class;
Initialization: Creates an empty list to store heap elements.
Heapify: Restores the heap property by comparing a node with its children and swapping if necessary. This is used internally to maintain the heap structure.
Insert: Adds a new element to the heap and then heapifies to maintain the heap property.
Extract Min: Removes and returns the minimum element (root) from the heap, replaces it with the last element, and heapifies to restore the heap property.


Find the Kth Largest Element using a Min Heap;
Import heapq: Imports the heapq module for heap operations.
Function definition: Defines the findKthLargest function with two parameters: nums (the input array) and k (the desired kth largest element).
Create a min heap: Initializes an empty list to represent the min heap.
Iterate through nums: For each number in the input array:
Pushes the negative of the number onto the heap using heapq.heappush. This effectively creates a max heap.
If the heap size exceeds k, remove the smallest element (largest negative number) using heapq.heappop.
Return the kth largest: Pops the largest element from the heap (the smallest negative number) and returns its absolute value.


Top K Frequent Elements;
Import necessary libraries: Imports heapq for heap operations and Counter for efficient counting.
Count frequencies: Creates a Counter object to count the frequency of each number in the input list nums.
Create a min heap: Builds a min heap of tuples (-freq, num) where freq is the frequency and num is the number. By negating the frequency, we effectively create a max heap based on frequency.
Extract top k elements: Uses heapq.nsmallest to extract the k smallest elements (highest frequencies) from the heap.
Return results: Returns a list of numbers corresponding to the top k frequent elements.


Merge K Sorted Lists using a Min Heap
Import heapq: Imports the heapq library for heap operations.
Function definition: Defines the mergeKLists function with a single parameter lists, which is a list of linked list heads.
Initialize heap: Creates an empty min heap heap.
Populate heap: Iterates through the input lists:
Checks if the current list is not empty.
If not empty, pushes a tuple (l.val, i, l) onto the heap.
l.val: Value of the current node in the list.
i: Index of the list in the lists array.
l: Reference to the current node in the list.
Dummy node: Creates a dummy node dummy to act as the head of the merged list.
Current node: Initializes a pointer cur to point to the dummy node.
Merge loop: While the heap is not empty:
val, i, node: Pops the minimum element (smallest value) from the heap.
val: Value of the minimum node.
i: Index of the list where the minimum node came from.
node: Reference to the minimum node.
Creates a new ListNode with the value val and assigns it to cur.next.
Updates cur to point to the newly created node.
Advances the pointer node to the next node in the list with index i.
If node is not empty (there are more elements in the list):
Pushes another tuple onto the heap representing the next node in the list (node.val, i, node).


Finding K Closest Points to the Origin
Import heapq: Imports the heapq module for heap operations.
Function definition: Defines the kClosest function with two parameters: points (a list of points as tuples) and k (the number of closest points to find).
Create a min heap: Initializes an empty min heap heap.
Calculate distances and populate heap: Iterates through each point (x, y) in points:
Calculates the squared distance to the origin (dist = x * x + y * y).
Pushes a tuple (dist, x, y) onto the heap. This effectively creates a min heap based on distances.
Maintain heap size: If the heap size exceeds k, removes the farthest point (largest distance) from the heap using heapq.heappop.
Return closest points: Extracts the k closest points from the heap using heapq.nsmallest and returns them as a list of tuples.
