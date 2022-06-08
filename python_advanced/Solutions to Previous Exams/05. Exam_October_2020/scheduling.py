from collections import deque

jobs = [int(job) for job in input().split(', ')]
index = int(input())

targeted_job = jobs[index]
sorted_jobs = deque(sorted(jobs))

cycles = 0

while True:
    job = sorted_jobs.popleft()
    if job == targeted_job:
        if job in sorted_jobs:
            cycles += job
        else:
            cycles += job
            break
    else:
        cycles += job

print(cycles)

