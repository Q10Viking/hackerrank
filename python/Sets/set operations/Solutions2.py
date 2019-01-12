n = int(input())
s = set(map(int, input().split())) 
methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}
for _ in range(int(input())):
    method, *args = input().split()
    methods[method](*map(int,args))