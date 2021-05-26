"""
--------------------------------------------------------------------Expected Solution-------------------------------------------------------------
"""
"""
# PF-Assgn-42
def find_factors(num):
    # Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2, (num + 1)):
        if (num % i == 0):
            factors.append(i)
    return factors



def is_prime(num, i):
    # Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if (i == 1):
        return True
    elif (num % i == 0):
        return False
    else:
        return (is_prime(num, i - 1))


def find_largest_prime_factor(list_of_factors):
    large = []
    for i in list_of_factors:
        if is_prime(i, i // 2) == True:
            large.append(i)
    return max(large)

    # Accepts the list of factors and returns the largest prime factor


def find_f(num):
    # Accepts the number and returns the largest prime factor of the number
    f = find_factors(num)
    l = find_largest_prime_factor(f)
    return l


def find_g(num):
    # Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sum = 0
    consicutive = [i for i in range(num, num + 9)]
    for i in consicutive:
        largest_prime_factor = find_f(i)
        sum = sum + largest_prime_factor
    return sum


# Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))
"""





"""
--------------------------------------------------------------------My Solution-------------------------------------------------------------
"""

#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    i = 0
    while i < len(list_of_factors):
        j = list_of_factors[i] // 2
        if is_prime(list_of_factors[i], j):
            i += 1
        else:
            list_of_factors.remove(list_of_factors[i])
    return max(list_of_factors)

def find_f(num):
    factors = find_factors(num)
    return factors

def find_g(num,counter):
    counter += 1
    if counter <= 9:
        factors = find_f(num)
        return find_largest_prime_factor(factors) + find_g(num+1,counter)
    else:
        return 0



#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10,0))