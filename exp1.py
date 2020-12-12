def fcfs(pid, n, bt):
    def waiting_time(pid, n, bt, wt):
        wt[0] = 0
        for i in range(1, n):
            wt[i] = bt[i-1] + wt[i-1]
    def turn_around_time(pid, n, bt, wt, tat):
        for i in range(n):
            tat[i] = wt[i] + bt[i]
    def avg_times(pid, n, bt):
        wt = [0]*n
        tat = [0]*n
        total_wt = 0
        total_tat = 0
        waiting_time(pid, n, bt, wt)
        turn_around_time(pid, n, bt, wt, tat)
        print("process ID " + " Burst time " + " Waiting time " + " Turn around time ")
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            print(" " + str(i+1) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
        print("Average waiting time = " + str(total_wt/n))
        print("Average turn around time = " + str(total_tat/n))
    avg_times(pid, n, bt)
pid = [1,2,3]
n = len(pid)
bt = [10,5,8]
fcfs(pid, n, bt)

def rr(pid, n, bt, time):
    def waiting_time(pid, n, bt, wt, time):
        bt2 = [0]*n
        for i in range(n):
             bt2[i] = bt[i]
        t = 0
        while(1):
            end = True
            for i in range(n):
                if bt2[i] > 0:
                    end = False
                    if bt2[i] > time:
                        bt2[i] = bt2[i] - time
                        t=t+time
                    else:
                        t=t+bt2[i]
                        wt[i] = t - bt[i]
                        bt2[i] = 0
            if end == True:
                break
    def turn_around_time(pid, n, bt, wt, tat):
        for i in range(n):
            tat[i] = wt[i] + bt[i]
    def avg_times(pid, n, bt):
        wt = [0]*n
        tat = [0]*n
        total_wt = 0
        total_tat = 0
        waiting_time(pid, n, bt, wt, time)
        turn_around_time(pid, n, bt, wt, tat)
        print("process ID " + " Burst time " + " Waiting time " + " Turn around time ")
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            print(" " + str(pid[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
        print("Average waiting time = " + str(total_wt/n))
        print("Average turn around time = " + str(total_tat/n))
    avg_times(pid, n, bt)
pid = [1,2,3]
n = len(pid)
bt = [10,5,8]
time = 3
rr(pid, n, bt, time)

#without arrival time
def sjf(pid, n, bt):
    def sort_sjf(pid, n, bt):
        for i in range(n):
            for j in range(0, n-i-1):
                if bt[j]>bt[j+1]:
                    bt[j], bt[j+1] = bt[j+1], bt[j]
                    pid[j], pid[j+1] = pid[j+1], pid[j]
    def waiting_time(pid, n, bt, wt):
        wt[0] = 0
        for i in range(1, n):
            wt[i] = bt[i-1] + wt[i-1]
    def turn_around_time(pid, n, bt, wt, tat):
        for i in range(n):
            tat[i] = wt[i] + bt[i]
    def avg_times(pid, n, bt):
        wt = [0]*n
        tat = [0]*n
        total_wt = 0
        total_tat = 0
        sort_sjf(pid, n, bt)
        waiting_time(pid, n, bt, wt)
        turn_around_time(pid, n, bt, wt, tat)
        print("process ID " + " Burst time " + " Waiting time " + " Turn around time ")
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            print(" " + str(pid[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
        print("Average waiting time = " + str(total_wt/n))
        print("Average turn around time = " + str(total_tat/n))
    avg_times(pid, n, bt)
pid = [1,2,3]
n = len(pid)
bt = [10,5,8]
sjf(pid, n, bt)