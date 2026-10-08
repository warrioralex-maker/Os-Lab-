#!/usr/bin/python3
processes =  ["P1", "P2","P3","P4"]
burst = [5,3,6,2]
priority = [3,1,2,4]

# Arrange processes according to priority
order = sorted(range(len(processes)), key=lambda i: priority[i])

time = 0

for i in order:
    ct = time + burst[i]
    tat = ct
    wt = tat - burst[i]

    print(processes[i], "CT =", ct, "TAT =", tat, "WT =", wt)

    time = ct
