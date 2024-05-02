n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
count = 1

for i in range(n):
    for j in range(n):
        arr[j][i] += count
        count += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()