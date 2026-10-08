#!/usr/bin/python3
processes = ["P1","P2","P3"]
burst = [5,3,8]
time =0
print("Process CT TAT WT")
for i in range (len(processes)):
    time+= burst[i]
    ct = time
    wt = ct - burst[i]
    print(processes[i],"  ",ct," ",wt)
