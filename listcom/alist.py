# alist.py
# assume we want to create a list of squares.
# range(2,10) using list comprehensions

# we could use loops like such
alist = []
for i in range(2,10):
  alist.append(i**2)
print(alist)
  
# using list comprehensions
alist = [i**2 for i in range(2,10)]
print(alist)
