def code(s, k):
    whole = list('abcdefghijklmnopqrstuvwxyz')
    slist = list(s)
    for i in range(0, len(s)):
        for j in range(0, 26):
            if s[i] == whole[j]:
                if j <= 26 - k:
                    slist[i] = whole[j+k]
                else:
                    slist[i] = whole[j+k-26]
    return ''.join(slist)

print(code('life', 2))
