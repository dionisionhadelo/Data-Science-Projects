rows = 6
k = rows
for i in range(rows, 0, -1):
    for j in range(0, k):
        print(end = " ")
    k += 1
    for j in range(0, i - 1):
        print(" *", end ="")
    print("")