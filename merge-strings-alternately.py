a = "abcd"
b = "pq"


n, m = len(a), len(b)
i, j = 0, 0
c = [0] * (n+m)

while i < n or j < m:
    if i < n:
        c.append(a[i])
        i += 1
    if j < m:
        c.append(b[j])
        j +=1

print(''.join(c))






