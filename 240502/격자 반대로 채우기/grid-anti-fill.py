n = int(input())

arr = [[1 for _ in range(n)] for _ in range(n)]

count = 0

for i in range(n-1, -1, -1):
    if (n - 1 - i) % 2 == 0:
        for j in range(n-1, -1, -1):
            arr[j][i] += count
            count += 1
    else:
        for j in range(n):
            arr[j][i] += count
            count += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()