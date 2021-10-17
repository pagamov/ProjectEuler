from lib import eratosthenes, prime, Pandig, pandig
from time import time

# Python3 program for the above approach
 
# Function to check if a
# number is prime or not
def isprm(n):
     
    # Base Case
    if (n <= 1):
        return 0
    if (n <= 3):
        return 1
    if (n % 2 == 0 or n % 3 == 0):
        return 0
 
    # Iterate till [5, sqrt(N)] to
    # detect primality of numbers
    i = 5
    while (i * i <= n):
 
        # If N is divisible by i
        # or i + 2
        if (n % i == 0 or
            n % (i + 2) == 0):
            return 0
         
        i = i + 6
     
    # Return 1 if N is prime
    return 1
 
# Function to count the prime numbers
# which can be expressed as sum of
# consecutive prime numbers
def countprime(n):
     
    # Initialize count as 0
    count = 0
 
    # Stores prime numbers
    primevector = []
 
    for i in range(2, n + 1):
 
        # If i is prime
        if (isprm(i) == 1):
            primevector.append(i)
         
    # Initialize the sum
    sum = primevector[0]
 
    # Find all required primes upto N
    for i in range(1, len(primevector)):
 
        # Add it to the sum
        sum += primevector[i]
        if (sum > n):
            break
        if (isprm(sum) == 1):
            count += 1
 
    # Return the final count
    return count
 
# Driver Code
 
# Given number N
N = 45
 
# Function call
print(countprime(N))
 
# This code is contributed by code_hunt