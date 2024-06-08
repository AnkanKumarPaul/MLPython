def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

p = 0.42
n = 8

# (a) Probability of getting a call from at least 3 universities
prob_at_least_3 = sum(combination(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(3, n + 1))

# (b) Probability of getting a call from exactly 4 universities
prob_exactly_4 = combination(n, 4) * (p ** 4) * ((1 - p) ** (n - 4))

print("Probability of getting call from at least 3 universities:", prob_at_least_3)
print("Probability of getting call from exactly 4 universities:", prob_exactly_4)
