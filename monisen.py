from math import sqrt


def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i ==0:
            return False
    return True



def monisen(no):
    P = 0
    n = 0
    while True:
        P += 1
        if isprime(P):
            M = 2**P-1
            if isprime(M):
                n += 1
                if n == int(no):
                    return M


print(monisen(input()))