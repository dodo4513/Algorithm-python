s = input()
i = 0
r = 0
while i < len(list(s)):
    if s[i:i + 2] == 'c=' \
            or s[i:i + 2] == 'c-' \
            or s[i:i + 2] == 's=' \
            or s[i:i + 2] == 'z=' \
            or s[i:i + 2] == 'd-' \
            or s[i:i + 2] == 'lj' \
            or s[i:i + 2] == 'nj':
        i += 1
    elif s[i:i + 3] == 'dz=':
        i += 2
    r += 1
    i += 1
print(r)
