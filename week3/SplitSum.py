'''
Question - 
  Write a Python function splitsum(l) that takes a nonempty list of integers and returns a list [pos,neg], 
  where pos is the sum of squares all the positive numbers in l and neg is the sum of cubes of all the negative numbers in l.
  Here are some examples to show how your function should work.
  
  >>> splitsum([1,3,-5])
  [10, -125]

  >>> splitsum([2,4,6])
  [56, 0]

  >>> splitsum([-19,-7,-6,0])
  [0, -7418]

  >>> splitsum([-1,2,3,-7])
  [13, -344]
  
'''

# SOLUTION - 

def splitsum(l):
  first = 0
  second = 0
  for each in l:
    if each < 0:
      first += (each*each*each)
    else:
      second += (each*each)
  return [second, first]
