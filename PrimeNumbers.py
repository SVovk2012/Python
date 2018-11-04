#function returns the list of prime numbers up to the 'num' and including 'num'
def count_primes(num):
    #initialize a list with first 2 known prime numbers:
    primenumberslist = [1,2]
    #iterate two times through all numbers up to the 'num'
    for a in range(3, num+1, 2):
        # change isprime to False if we find that the number could be devided without remainder by some other number
        isprime = True
        for b in range(3,a):
            if a%b==0 and a!=b:
                isprime = False
                break
        #append to the list of primes if we did't prove that it is not prime (isprime == True)
        if isprime:
            primenumberslist.append(a)
              
        
    return primenumberslist


count_primes(100)
