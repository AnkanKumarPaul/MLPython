import math

def exponential_pdf(rate, x):
    return rate * math.exp(-rate * x)

# (a) Calculate the probability that the system will fail before 85 hrs.
MTBF = 85
prob_fail_before_85 = 1 - math.exp(-1 / MTBF * 85)

# (b) Calculate the probability that it will not fail up to 150 hrs.
prob_not_fail_up_to_150 = math.exp(-1 / MTBF * 150)

print("Probability that the system will fail before 85 hrs:", prob_fail_before_85)
print("Probability that it will not fail up to 150 hrs:", prob_not_fail_up_to_150)
