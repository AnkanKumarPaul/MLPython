import math

sample_mean = 4998.1
population_std_dev = 1.30
sample_size = 60
population_mean = 5000

z_score = (sample_mean - population_mean) / (population_std_dev / math.sqrt(sample_size))

alpha = 0.05

critical_z_value = -1.645

if z_score <= critical_z_value:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print("Z-score:", z_score)
