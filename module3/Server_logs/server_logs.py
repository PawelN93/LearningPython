logs = []
with open("server_logs.txt") as file:
    logs = file.readlines()

print(logs)
num_of_requests = len(logs)
num_of_positive_requests = 0
num_of_negative_requests = 0

for log in logs:
    # log_value = int(log.removesuffix("\n")[-3:])
    _, _, _, log_value = log.split()
    log_value = int(log_value)
    if log_value in range(200, 300):
        num_of_positive_requests += 1
    elif log_value in range(400, 600):
        num_of_negative_requests += 1

with open("report.txt", 'w') as file:
    file.write("Amount of tries: " + str(num_of_requests) + "\n")
    file.write("Amount of positive tries: " + str(num_of_positive_requests) + "\n")
    file.write("Amount of negative tries: " + str(num_of_negative_requests) + "\n")

print("Amount of tries: " + str(num_of_requests))
print("Amount of positive tries: " + str(num_of_positive_requests))
print("Amount of negative tries: " + str(num_of_negative_requests))
