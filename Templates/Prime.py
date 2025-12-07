########################
# Precomputed Versions #
########################

m = 10 ** 6


# Prime Sieve
is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, m + 1) if is_prime[i]]


# Smallest Prime Factor (SPF)
spf = list(range(m + 1))
for i in range(2, int(m ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, m + 1, i):
            if spf[j] == j:
                spf[j] = i


# Factorization
def factorize(x: int):
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        yield p, cnt


# Prime factors (with multiplicity)
def factors(x: int):
    while x > 1:
        p = spf[x]
        yield p
        x //= p


# Square-free core
core = [0] * (m + 1)
for i in range(1, m + 1):
    if core[i] == 0:
        for j in range(1, int(((m + 1) // i) ** 0.5) + 1):
            core[i * j * j] = i


# ####################
# On-Demand Versions #
# ####################

def is_prime_naive(x: int) -> bool:
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def smallest_prime_factor_naive(x: int):
    if x < 2:
        return None
    if x % 2 == 0:
        return 2
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return i
    return x


def factorize_naive(x: int):
    i = 2
    while i * i <= x:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                x //= i
                cnt += 1
            yield i, cnt
        i += 1
    if x > 1:
        yield x, 1


def factors_naive(x: int):
    i = 2
    while i * i <= x:
        while x % i == 0:
            yield i
            x //= i
        i += 1
    if x > 1:
        yield x


def squarefree_core_naive(x: int):
    res = 1
    for p, cnt in factorize_naive(x):
        if cnt % 2 == 1:
            res *= p
    return res


#################
# Example Usage #
#################
if __name__ == "__main__":
    n = 360
    print("--- Precomputed ---")
    print("is_prime[37] =", is_prime[37])
    print("spf[360] =", spf[360])
    print("factorize:", list(factorize(n)))
    print("factors:", list(factors(n)))
    print("core[360] =", core[360])

    print("\n--- On-demand ---")
    print("is_prime_naive(37):", is_prime_naive(37))
    print("smallest_prime_factor_naive(84):", smallest_prime_factor_naive(84))
    print("factorize_naive:", list(factorize_naive(n)))
    print("factors_naive:", list(factors_naive(n)))
    print("squarefree_core_naive(360):", squarefree_core_naive(n))
