count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)

start=count_all
max=len(count_all)
i=0
while True:
    prev=start
    if i<max:
        start=start[i]
    else:
        start=prev
    i+=1