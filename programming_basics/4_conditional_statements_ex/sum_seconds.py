first_runner = int(input())
second_runner = int(input())
third_runner = int(input())
import math

total_time = first_runner + second_runner + third_runner
minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

