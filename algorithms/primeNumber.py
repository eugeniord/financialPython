

def isPrime(number):
    if number%2==0: return False
    for i in range (3, int(number**0.5), 2):
        if number%i == 0: return False
    return True