import random
class Solution(object):
  def quickSort(self, array):
    if array == []:
      return array
    self.sort(array, 0, len(array)-1)
    return array   
    
    # write your solution here
  def sort(self, array, start, end):
    if start >= end:
      return
    if start == end - 1:
      if array[start] > array[end]:
       	self.swap(array, start, end)
      return
    p = end #random.randint(start, end + 1)
    self.swap(array, p, end)
    i = start
    j = end - 1
    while i <= j:
      if array[i] > array[end] and array[j] < array[end]:
       	self.swap(array, i, j)
        i += 1
        j -= 1
      if array[i] <= array[end]:
        i += 1
      # either put the equal one on the right or swap!
      # otherwise there will be a dead loop
      # example: (10, 8, 10, 8)
      if array[j] >= array[end]:   
        j -= 1
      
    self.swap(array, i, end)
    self.sort(array, start, i-1)
    self.sort(array, i+1, end)
      
  def swap(self, array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
