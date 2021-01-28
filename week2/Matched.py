# Second Problem:
'''
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, 
every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. 
Your function should return True if s has matched brackets and False if it does not.
'''

# SOLUTION - 

def matched(s):
  a = 0
  for each in s:
    if each == '(':
      a += 1
    if each == ')':
      a -= 1
    if a < 0:
      return False
  if a != 0:
    return False
  return True
