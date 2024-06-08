sample_size = 100
defective_count = 22

null_proportion = 0.18

sample_proportion = defective_count / sample_size

z_score = (sample_proportion - null_proportion) / ((null_proportion * (1 - null_proportion)) ** 0.5 / sample_size ** 0.5)

alpha = 0.05

critical_z_value = -1.645

if z_score <= critical_z_value:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print("Z-score:", z_score)
