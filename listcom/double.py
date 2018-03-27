
# list comprehension in functions.

def double(numero):
  return numero**2
  
print(double(3))

# We can easily use list comprehension on that function.

result = [double(numero) for numero in range(10)]

print(result)
