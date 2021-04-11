# FIRST_FIT
blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)

allocation = [-1] * n

for i in range(n):
    for j in range(m):
        if blockSize[j] >= processSize[i]:
            allocation[i] = j
            blockSize[j] -= processSize[i]
            break

print("\n\n                FIRST FIT")
print(" Process No.  Process Size     Block No.")
for i in range(n):
    print(" ",i+1,"          ",processSize[i],"           ",end=" ")
    if allocation[i] != -1:
        print(allocation[i] +1)
    else:
        print("Not Allocated")



# BEST FIT
blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)

allocation = [-1] * n

for i in range(n):
    bestIdx = -1
    for j in range(m):
        if blockSize[j] >= processSize[i]:
            if bestIdx == -1:
                bestIdx = j
            elif blockSize[bestIdx] > blockSize[j]:
                bestIdx = j
                
    if bestIdx != -1:
        allocation[i] = bestIdx
        blockSize[bestIdx] -= processSize[i]

print("\n\n                BEST FIT")
print(" Process No.  Process Size     Block No.")
for i in range(n):
    print(" ",i+1,"          ",processSize[i],"           ",end=" ")
    if allocation[i] != -1:
        print(allocation[i] +1)
    else:
        print("Not Allocated")



# WORST FIT
blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)

allocation = [-1] * n

for i in range(n):
    wstIdx = -1
    for j in range(m):
        if blockSize[j] >= processSize[i]:
            if wstIdx == -1:
                wstIdx = j
            elif blockSize[wstIdx] < blockSize[j]:
                wstIdx = j
                
    if wstIdx != -1:
        allocation[i] = wstIdx
        blockSize[wstIdx] -= processSize[i]

print("\n\n                WORST FIT")
print(" Process No.  Process Size     Block No.")
for i in range(n):
    print(" ",i+1,"          ",processSize[i],"           ",end=" ")
    if allocation[i] != -1:
        print(allocation[i] +1)
    else:
        print("Not Allocated")



# NEXT FIT
blockSize = [5, 10, 20, 30, 40]
processSize = [6, 4, 14, 8, 9]
m = len(blockSize)
n = len(processSize)

allocation = [-1] * n
j = 0

for i in range(n):
    while j < m:
        if blockSize[j] >= processSize[i]:
            allocation[i] = j
            blockSize[j] -= processSize[i]
            break
        j = (j+1)%m
print("\n\n                NEXT FIT")
print(" Process No.  Process Size     Block No.")
for i in range(n):
    print(" ",i+1,"           ",processSize[i],"            ",end=" ")
    if allocation[i] != -1:
        print(allocation[i] +1)
    else:
        print("Not Allocated")
