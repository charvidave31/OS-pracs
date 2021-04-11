from scheduler import fcfs,sjf,p,rr 

processes = [1,2,3]
n=len(processes)
bt=[10,5,8]
fcfs(processes,n,bt)
rr(processes,n,bt,2)
sjf(processes,n,bt)

processes = [1,2,3]
n=len(processes)
priority= [2,3,1]
bt=[10,5,8]
p(processes,n,bt,priority)