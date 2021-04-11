def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def sort_aesc(pid, n, bt, at):
	for i in range(n-1):
		if bt[i] > bt[i+1]:
			swap(pid, i, i+1)
			swap(bt, i, i+1)
			swap(at, i, i+1)

def sort_wt(pid, n, bt, at, wt):
	for i in range(n-1):
		if wt[i] > wt[i+1]:
			swap(pid, i, i+1)
			swap(bt, i, i+1)
			swap(at, i, i+1)
			swap(wt, i, i+1)

def turn_around_time(pid, n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]

# Shortest Job First
def sjf_waiting_time(pid, n, bt, at, max_t,wt):
	t_elapsed = 0
	while (t_elapsed < max_t):
		for i in range(n):
			if t_elapsed == max_t:
				break
			if at[i] <= t_elapsed and wt[i] == 0:
				wt[i] = t_elapsed 
				t_elapsed = t_elapsed + bt[i]

def sjf(pid, n, bt, at):
	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0
	max_t = 0
	n_pid = [0] * n
	n_bt = [0] * n
	n_at = [0] * n

	for i in range(n):
		n_pid[i] = pid[i]
		n_bt[i] = bt[i]
		n_at[i] = at[i]
		max_t = max_t + bt[i]

	sort_aesc(n_pid, n, n_bt, n_at)
	sjf_waiting_time(n_pid, n, n_bt, n_at, max_t, wt)
	sort_wt(n_pid, n, n_bt, n_at, wt)
	turn_around_time(n_pid, n, n_bt, wt, tat)
	# Display
	print("Shortest Job First:")
	print("Process ID"+"\t Arrival Time"+"\t Burst Time"+"\t Waiting Time"+"\t Turn Around Time")
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(n_pid[i],"\t\t",n_at[i],"\t\t",n_bt[i],"\t\t",wt[i],"\t\t",tat[i])

	print("\nAverage Waiting Time : ", (total_wt/n))
	print("Average Turn Around Time: ", (total_tat/n))

# Round Robin 
def rr_waiting_time(pid, n, bt, at, wt, t_interval = 2):
    re_bt = [0] * n
    t = 0
    for i in range(n):
        re_bt[i] = bt[i]
 
    while(1):
        done = True
        for i in range(n):
            if ((re_bt[i] > 0) and (at[i] <= t)):
                done = False
                if (re_bt[i] > t_interval):
                    t = t + t_interval
                    re_bt[i] = re_bt[i] - t_interval
                else:
                    t = t + re_bt[i]
                    wt[i] = t - bt[i] - at[i]
                    re_bt[i] = 0
        if (done == True):
            break
                    

def round_robin(pid, n, bt, at, t_interval = 2):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    rr_waiting_time(pid, n, bt, at, wt, t_interval)
    turn_around_time(pid, n, bt, wt, tat)
    # Display
    print("\nRound Robin: ")
    print("Process ID"+"\t Arrival Time"+"\t Burst Time"+"\t Waiting Time"+"\t Turn Around Time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(pid[i],"\t\t",at[i],"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i])

    print("\nAverage Waiting Time : ", (total_wt/n))
    print("Average Turn Around Time: ", (total_tat/n))