# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:22:21 2020

@author: Charvi
"""


def fcfs(p_id,n,b_t):
    w_t=[]
    w_t[0]=0
    for i in range(1,n):
        w_t[i]=b_t[i-1] + w_t[i-1]
    for i in range(n):
        ta_t[i]= b_t[i] + w_t[i]
    avg_wt=mean(w_t)
    avg_tat=mean(ta_t)
    print("Processes ", p_id)
    print("Burst Time " , b_t)
    print("Waiting Time " , w_t)
    print("Turn Around Time " , ta_t)
    print("Average Waiting Time: " , avg_wt)
    print("Average Turn Around Time: " , avg_tat)
    
    