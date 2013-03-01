def get_prime_values():
    def isprime(n):
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                return False
        return True

    data_list = []
    num=600851475143
    for i in xrange(2, 10000):
        if isprime(i) and num%i==0:
            data_list.append(i)
    return max(data_list)

print get_prime_values()