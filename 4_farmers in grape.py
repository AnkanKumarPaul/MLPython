import math

def standard_normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

mean = 38
std_dev = 5

# (a) Proportion of farmers spraying more than 50 liters of pesticide in a week
z_score_50 = (50 - mean) / std_dev
prop_more_than_50 = 1 - standard_normal_cdf(z_score_50)

# (b) Proportion of farmers spraying less than 10 liters of pesticide in a week
z_score_10 = (10 - mean) / std_dev
prop_less_than_10 = standard_normal_cdf(z_score_10)

# (c) Proportion of farmers spraying between 30 liters and 60 liters of pesticide in a week
z_score_30 = (30 - mean) / std_dev
z_score_60 = (60 - mean) / std_dev
prop_between_30_and_60 = standard_normal_cdf(z_score_60) - standard_normal_cdf(z_score_30)

print("Proportion of farmers spraying more than 50 liters:", prop_more_than_50)
print("Proportion of farmers spraying less than 10 liters:", prop_less_than_10)
print("Proportion of farmers spraying between 30 and 60 liters:", prop_between_30_and_60)
