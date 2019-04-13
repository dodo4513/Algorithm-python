t = input()
for i in range(1, int(t) + 1):
    input()
    s = input()
    print("Case #" + str(i) + ": ", end='')
    for j in list(s):
        if j == 'E':
            print('S', end='')
        else:
            print('E', end='')
    print()

'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

2
2
SE
5
EESSSESE
'''