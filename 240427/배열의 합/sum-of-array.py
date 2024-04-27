arr_2d = []

for i in range(4):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for i in range(4):
    print(sum(arr_2d[i]))