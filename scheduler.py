#FIRST COME FIRST SERVE
def fcfs(procs,n,bt):
    wt = [0] * n
    tat = [0] *n
    total_wt = 0
    total_tat = 0
    
    wt[0]=0
    
    #wating time
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]
        
    #turn around time
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    
    print("\n\n\tFIRST COME FIRST SERVE CPU")
    print("Processes Burst Time " + " Waiting Time " + " Turn around time")
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("/t" +str(procs[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t " + str(tat[i]))
    
    print("Average Waiting time = "+ str(total_wt/n))
    print("Average Turn Around time = "+ str(total_tat/n))
    
#SHORTEST JOB FIRST
def sjf(procs,n,bt):
    wt = [0]*n
    tat = [0]*n
    total_wt = 0
    total_tat = 0
    
    wt[0]=0
    bt2=bt
    
    for i in range(len(bt)):
        min = i
        for j in range(i+1, len(bt)):
            if bt[j]<bt[min]:
                min = j
        bt[i],bt[min] = bt[min],bt[i]
        procs[i],procs[min] = procs[min],procs[i]
    
    #wating time
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]
        
    #turn around time
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    
    print("\n\n\t  SHORTEST JOB FIRST CPU")
    print("Processes Burst Time " + " Waiting Time " + " Turn around time")
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("/t" +str(procs[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t " + str(tat[i]))
    
    print("Average Waiting time = "+ str(total_wt/n))
    print("Average Turn Around time = "+ str(total_tat/n))
    

#PRIORITY
def p(procs,n,bt,pr):
    wt = [0]*n
    tat = [0]*n
    total_wt = 0
    total_tat = 0
    
    wt[0]=0
    bt2=bt
    
    for i in range(len(pr)):
        min = i
        for j in range(i+1, len(pr)):
            if pr[j]<pr[min]:
                min = j
        pr[i],pr[min] = pr[min],pr[i]
        bt[i],bt[min] = bt[min],bt[i]
        procs[i],procs[min] = procs[min],procs[i]
    
    #wating time
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]
        
    #turn around time
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    
    print("\n\n\t\tPRIORITY CPU")
    print("Processes Burst Time " + " Waiting Time " + " Turn around time")
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("/t" +str(procs[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t " + str(tat[i]))
    
    print("Average Waiting time = "+ str(total_wt/n))
    print("Average Turn Around time = "+ str(total_tat/n))
    

#ROUND ROBIN
def rr(procs,n,bt,quantum):
    wt = [0]*n
    tat = [0]*n
    rem_bt = [0]*n
    total_wt = 0
    total_tat = 0
    
    for i in range(n):
        rem_bt[i]=bt[i] 
    
    t=0 #total table
    
    while(1): 
        done = True
  
        for i in range(n): 
              
            if (rem_bt[i] > 0) : 
                done = False # There is a pending process 
                  
                if (rem_bt[i] > quantum) : 
                    
                    t += quantum
                    rem_bt[i] -= quantum  
                   
                else: 
                    
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
                    
        # If all processes are done  
        if (done == True): 
            break
    
    #turn around time
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    
    print("\n\n\t\tROUND ROBIN")
    print("Processes Burst Time " + " Waiting Time " + " Turn around time")
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + wt[i]
        print("/t" +str(procs[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t " + str(tat[i]))
    
    print("Average Waiting time = "+ str(total_wt/n))
    print("Average Turn Around time = "+ str(total_tat/n))