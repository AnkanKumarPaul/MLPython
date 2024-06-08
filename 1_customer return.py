import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def poisson_pmf(rate, k):
    return (rate ** k) * math.exp(-rate) / factorial(k)

# (a) Calculate the probability that the number of returns exceeds 30 in a day
rate = 25
prob_exceed_30 = 1 - sum(poisson_pmf(rate, i) for i in range(31))

# (b) Calculate the probability that there will be at least 2 fraudulent returns in any given day
chance_fraudulent = 0.05
prob_at_least_2_fraudulent = 1 - (poisson_pmf(chance_fraudulent * rate, 0) + poisson_pmf(chance_fraudulent * rate, 1))

print("Probability that the number of returns exceeds 30 in a day:", prob_exceed_30)
print("Probability that there will be at least 2 fraudulent returns in any given day:", prob_at_least_2_fraudulent)
