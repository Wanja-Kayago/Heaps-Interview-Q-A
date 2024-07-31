# Implement a Min Heap

import heapq

class MinHeap:
    def __init__(self):
        self.h = []

    def heapify(self, i):
        n = len(self.h)
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.h[l] < self.h[largest]:
            largest = l

        if r < n and self.h[r] < self.h[largest]:
            largest = r

        if largest != i:
            self.h[i], self.h[largest] = self.h[largest], self.h[i]
            self.heapify(i)

    def insert(self, val):
        self.h.append(val)
        n = len(self.h)
        i = n // 2 - 1
        while i >= 0:
            self.heapify(i)
            i -= 1

    def extract_min(self):
        if not self.h:
            return None
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        min_val = self.h.pop()
        self.heapify(0)
        return min_val


#  Find the Kth Largest Element in an Array
import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return -heapq.heappop(heap)


# Top K Frequent Elements
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(heap)
    return [num for _, num in heapq.nsmallest(k, heap)]


# Merge K Sorted Lists
import heapq

def mergeKLists(lists):
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
    dummy = ListNode()
    cur = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = ListNode(val)
        cur = cur.next
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))
    return dummy.next


#  K Closest Points to Origin
import heapq

def kClosest(points, k):
    heap = []
    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (dist, x, y))
    return [(x, y) for _, x, y in heapq.nsmallest(k, heap)]
