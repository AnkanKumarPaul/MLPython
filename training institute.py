def read_csv(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(',') for line in lines[1:]]
        return data

def calculate_mean(data):
    total = sum(data)
    return total / len(data)

def calculate_differences(data):
    differences = []
    for pair in data:
        differences.append(float(pair[1]) - float(pair[0]))
    return differences

def calculate_std_dev(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return variance ** 0.5

def calculate_t_statistic(mean_diff, std_dev_diff, n):
    standard_error = std_dev_diff / (n ** 0.5)
    return mean_diff / standard_error

def calculate_degrees_of_freedom(n):
    return n - 1

critical_t_value = 1.699127

data = read_csv('trainingscores.csv')

differences = calculate_differences(data)

mean_diff = calculate_mean(differences)

std_dev_diff = calculate_std_dev(differences, mean_diff)

n = len(differences)

t_statistic = calculate_t_statistic(mean_diff, std_dev_diff, n)

df = calculate_degrees_of_freedom(n)

if t_statistic > critical_t_value:
    print("Reject the null hypothesis. Training is effective.")
else:
    print("Fail to reject the null hypothesis. Training is not effective.")

print("t-statistic:", t_statistic)
print("Critical t-value:", critical_t_value)
#no csv,no run