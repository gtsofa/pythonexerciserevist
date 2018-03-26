# implementation
'''
A prime number is only evenly divisible by itself and 1.
Note that 1 is not a prime number. create a function that generates prime numbers.
Eg prime_list =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
'''

# Python Program - Print Prime Numbers

#import math
def primeNumbers(n):
    '''
    Returns a list of prime numbers.
    '''
    prime_list = []
    
    for i in range(2,n+1):
        
        primeflag = True
        
        for num in prime_list:
            
            if(i%num ==0):
                
                primeflag=False
                
        if(primeflag):
            
            prime_list.append(i)
            
    return prime_list

# test for methods here.
print(primeNumbers(10))
print(primeNumbers(30))
