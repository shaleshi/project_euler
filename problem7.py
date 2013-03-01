def get_prime_values():
    def isprime(n):
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                return False
        return True

    data_list = []

    for i in xrange(2, 500000):
        if isprime(i):
            data_list.append(i)
        if len(data_list) == 10001:
            return i

print get_prime_values()
