n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr1[i][j] != arr2[i][j]:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()