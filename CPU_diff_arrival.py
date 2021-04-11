from scheduler_diff_arrival import sjf, round_robin

pid = [1,2,3,4,5]
n = len(pid)
at = [2, 0, 0, 1, 5]
bt = [5, 8, 4, 1, 3]

sjf(pid, n, bt, at)

pid = [1,2,3,4,5]
n = len(pid)
at = [2, 0, 0, 1, 5]
bt = [5, 8, 4, 1, 3]
round_robin(pid, n, bt, at, 2)