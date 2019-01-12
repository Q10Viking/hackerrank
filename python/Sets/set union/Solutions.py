# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b,c,d = (input() for _ in range(4))

b = set(b.split())
d = set(d.split())

print(len(b.union(d)))