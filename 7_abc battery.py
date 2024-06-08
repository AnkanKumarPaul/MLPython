sample_size = 100
abc_sample_mean = 450
competitor_sample_mean = 368
competitor_sample_std_dev = 78

claimed_difference = 60

z_score = ((abc_sample_mean - competitor_sample_mean) - claimed_difference) / (competitor_sample_std_dev / (sample_size ** 0.5))

alpha = 0.05

critical_z_value = 1.645

if z_score >= critical_z_value:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print("Z-score:", z_score)
