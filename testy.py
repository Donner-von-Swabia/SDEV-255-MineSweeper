import random
import time
list1=[0,1,0,0,0,0,0]
start=time.time()
total = 0
min = 0 
max = 64
rows = []
column = []
for i in range(min,max):
    for j in range(min,max):
        num = random.choice(list1)
        if num == 1:
            total= total +1
            column.append(9)
        else:
            column.append(0)  
    rows.append(column)
    column = []
for i in range(min,max):
    for j in range(min,max):
        if (rows[i])[j] == 9:
            if i > 0 and i < len(rows):
                if (rows[(i-1)])[j-1] != 9:
                    (rows[(i-1)])[j-1]+= 1
                if (rows[i-1])[j] != 9:
                    (rows[i-1])[j]+= 1
                if j < (max -1):
                    if (rows[i-1])[j+1] != 9:
                        (rows[i-1])[j+1]+= 1
                    if i < (max-1):
                        if (rows[i+1])[j+1] != 9:
                            (rows[i+1])[j+1]+= 1
                if i < (max-1):
                    if (rows[(i+1)])[j-1] != 9:
                        (rows[(i+1)])[j-1]+= 1
                    if (rows[(i+1)])[j] != 9:
                        (rows[(i+1)])[j]+= 1
                
            if j > 0 and j < max-1:
                if (rows[(i)])[j-1] != 9:
                    (rows[(i)])[j-1]+= 1
                if (rows[(i)])[j+1] != 9:
                    (rows[(i)])[j+1]+= 1
            
for i in range(min,max):
    print(rows[i])
end = time.time()
print(end-start)
print((rows[2])[2])
print(total)