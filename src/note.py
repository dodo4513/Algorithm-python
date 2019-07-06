t = int(input())
for _ in range(t):
    c, l = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    sums = [0] * 1001
    sums[1] = arr[0]
    for i in range(1, len(arr)):
        sums[i + 1] = sums[i] + arr[i]

    r = 9999
    for day in range(l, len(arr) + 1):
        for i in range(0, len(arr) - day + 1):
            cSum = sums[i + day] - sums[i]
            r = min(r, cSum / day)
    print("%.10f" % r)
