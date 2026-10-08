#!/usr/bin/python3
from collections import deque
processes = ["P1", "P2", "P3"]

# Burst time of each process
burst = {
    "P1": 5,
    "P2": 3,
    "P3": 6
}

# Time given to each process in one turn
quantum = 2

# Create a queue containing all processes
queue = deque(processes)

# Make a copy of burst time
# This will keep track of the remaining burst time
remaining = burst.copy()

# Starting CPU time
time = 0

# Continue until the queue becomes empty
while queue:

    # Take the first process from the queue
    p = queue.popleft()

    # If the remaining burst time is greater than quantum
    if remaining[p] > quantum:

        # Give the process one quantum of CPU time
        time += quantum

        # Reduce its remaining burst time
        remaining[p] -= quantum

        # Process is not finished
       # So put it at the end of the queue
        queue.append(p)

    else:

        # Process can finish in this turn
        time += remaining[p]

        # Set remaining burst time to 0
        remaining[p] = 0

        # Display completion time
        print(p, "completed at", time)

# Note: Small quantum = fairer but more switching; large quantum acts like FCFS.
