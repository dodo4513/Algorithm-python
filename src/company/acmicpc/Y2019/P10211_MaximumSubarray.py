t = input()
for t in range(0, int(t)):
    input()
    arr = list(map(int, input().split()))
    max = -9999

    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, -1, -1):
            sum += arr[j]
            if sum > max:
                max = sum
    print(max)
