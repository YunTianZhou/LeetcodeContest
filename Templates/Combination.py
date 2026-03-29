m = 10 ** 5
mod = 10 ** 9 + 7

fact = [1] * (m + 1)
inv_fact = [1] * (m + 1)

for i in range(1, m + 1):
    fact[i] = fact[i - 1] * i % mod

inv_fact[m] = pow(fact[m], mod - 2, mod)
for i in range(m - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] * inv_fact[n - r] % mod

def perm(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[n - r] % mod
