def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


t = input()
for i in range(1, int(t) + 1):
    N, L = input().split()
    arr = list(map(int, input().split()))
    r = []

    j = 0
    for j in range(0, len(arr) - 1):
        if arr[j] == arr[j + 1]:
            continue

        key = gcd(arr[j], arr[j + 1])
        r.append(arr[j] // key)
        r.append(key)
        for k in range(j + 1, len(arr)):
            key = arr[k] // key
            r.append(key)

        break

    for l in range(j, 0, -1):
        r.insert(0, arr[l - 1] // r[0])

    table = sorted(set(r[:]))

    print('Case #' + str(i) + ': ', end='')
    for j in range(0, len(r)):
        print(chr(ord('A') + table.index(r[j])), end='')
    print()

'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
'''