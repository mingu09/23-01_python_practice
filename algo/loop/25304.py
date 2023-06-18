x = int(input())
n = int(input())
s = 0
for i in range(n):
    a ,b = map(int ,input().split(' '))
    s = s + a * b
print(s) 
if s == x:
    print("Yes")
else :
    print("No")