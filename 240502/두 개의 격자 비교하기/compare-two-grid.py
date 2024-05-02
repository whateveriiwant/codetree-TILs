n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2.append(list(map(int, input().split())))

arr3 = [
    [1 if arr1[i][j] != arr2[i][j] else 0 for j in range(m)]
    for i in range(n)
]

for i in range(n):
    for j in range(n):
        print(arr3[i][j], end=" ")
    print()