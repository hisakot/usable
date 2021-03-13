import math

h_start = [10.30, 11.55, 11.15, 11.15, 11.30, 11.30, 11.30]
h_end = [19.30, 19.45, 14.50, 17.00, 17.00, 17.00, 17.00]

w_start = [17.00]
w_end = [20.40]

def time_to_hour(times):
    hours = list()
    for time in times:
        i = int(time)
        f = time - int(time)
        time = round(i + f * 100 / 60, 3)
        hours.append(time)
    return hours

h_start = time_to_hour(h_start)
h_end = time_to_hour(h_end)

w_start = time_to_hour(w_start)
w_end = time_to_hour(w_end)

salary = 0
for i, s_time in enumerate(h_start):
    work = h_end[i] - s_time
    if work >= 8:
        work -= 1
    salary += work * 1200
for i, s_time in enumerate(w_start):
    work = w_end[i] - s_time
    if work >= 8:
        work -= 1
    salary += work * 1100
print(salary)
