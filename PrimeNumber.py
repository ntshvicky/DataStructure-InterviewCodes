# find prime number
N = int(input("Enter a number: "))


# Way 1:-
arr = [2]
for i in range(3, N + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        arr.append(i)

print(arr)

## Time complexity - 
    based on N/2 nos of iteration its O(N)
    based on inner N*N - because i*N - O(N^2)
    Total - O(N) + O(N^2) = O(N^3)
            
## Space complexity - O(N)

# Way 2:-
arr = [2]
for i in range(3, N + 1, 2):
    isPrime = True
    for j in range(2, int(i/2)):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        arr.append(i)

print(arr)

## Time complexity - 
    based on N/2 nos of iteration its O(N/2)
    based on inner (N*N)/2 - its like 2 to i/2 - i*N/2 so O(N^2/8)
    Total - O(N/2) + O(N^2/8) - O(N^2)
            
## Space complexity - O(N)


## Way 3
def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1) # True in array N times pre filled
    primes[0] = primes[1] = False  # 0 and 1 are not primes 

    p = 2 # start with 2
    while p * p <= N:
        if primes[p]: # if an index of array already set true
            for i in range(p * p, N + 1, p): # like if p is 2 , then all step 2 is devisable of 2 , same 3 
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, N + 1):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers

N = int(input("Enter a number N: "))
prime_numbers = sieve_of_eratosthenes(N)
print(prime_numbers)

## Time complexity - O(Nlog(logN))
## Space complexity - O (N)

### all has space complexity O(N) because all need the same array of storage