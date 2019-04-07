def make_power(a,n):
    d = 1.0
    for x in range(1,n+1):
        d=float(d*a)
    return d


arr = [int(y) for y in input().split()]
w = float(arr[0])
z = int(arr[1])
result = make_power(w,z)
print(result)