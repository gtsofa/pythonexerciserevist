# alist.py
# assume we want to create a list of squares.
# range(2,10) using list comprehensions

# we could use loops like such
alist = []
for i in range(2,10):
  alist.append(i**2)
print(alist)
  
# using list comprehensions
# FYI: Just remember the syntax: [ expression for item in list if conditional ]
'''
What is a list comprehension?
A list comprehension is a special brackety syntax to perform a transform operation with 
an optional filter clause that always produces a new sequence (list) object as a result. 
To break it down visually, you perform:

new_range = [i * i          for i in range(5)   if i % 2 == 0]
Which corresponds to:

*result*  = [*transform*    *iteration*         *filter*     ]
The filter piece answers the question, "should this item be transformed?" If the answer is yes,
then the transform piece is evaluated and becomes an element in the result. 
The iteration [*] order is preserved in the result.
'''
alist = [i**2 for i in range(2,10)]
print(alist)
