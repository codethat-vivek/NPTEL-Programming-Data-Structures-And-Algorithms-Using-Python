'''
Question - 
  Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the last occurrence of each number. 
  For instance:
  >>> remdup([3,1,3,5])
  [3, 1, 5]

  >>> remdup([7,3,-1,-5])
  [7, 3, -1, -5]

  >>> remdup([3,5,7,5,3,7,10])
  [5, 3, 7, 10]
  
'''

# SOLUTION - 

def remdup(l):
  lt = []
  for i in range(len(l)-1, -1, -1):
    if l[i] not in lt:
      lt.append(l[i])
  return lt[::-1]
  
 
