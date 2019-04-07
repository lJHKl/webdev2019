def find_minimum(a,b,c,d):
    if a > b:
        a,b = b,a
    elif a > c:
        a,c = c,a
    elif a > d:
        a,d = d,a
    elif b > c:
        b,c = c,b
    elif b > d:
        b,d = d,b
    elif c > d:
        c,d = d,c
    return a


arr = [int(x) for x in input().split()]

m = find_minimum(arr[0],arr[1],arr[2],arr[3])
print(m)
