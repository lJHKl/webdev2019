a = int(input())

arr = []

for i in range(0,a):
    arr.append(int(input()))

print([i for i in a if i%2 == 0])