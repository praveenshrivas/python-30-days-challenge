n = int(input())

arr = list(map(int, input().split()))

print(' '.join(map(str,arr[::-1])))
