phone_book = {}

# Read number of entries
n = int(input())

# Read and store phone book entries
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Process queries until EOF
try:
    while True:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
