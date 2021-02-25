#primes.py
#generate primes in a function
#Shane Austin


primes = []
upto = 101


for candidate in range (2,upto):
     #print(candidate)
    isPrime = True
    for divisor in primes:
        if (candidate % divisor == 0):
            isPrime = False
            break

    if isPrime:
        primes.append(candidate)

print (primes)
