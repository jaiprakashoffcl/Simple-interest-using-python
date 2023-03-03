import heapq
 

def find_smallest(numbers):

    heap = [(x, x) for x in numbers]

    heapq.heapify(heap)

     

   _,smallest = heapq.heappop(heap)

     

   return smallest
 
numbers = [10, 20, 4, 45, 99]

print(find_smallest(numbers)) 
