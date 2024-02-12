x = 4
print(type(x))

a=1
arr=[1,2,3]
print(id(a)==id(arr[0]))
l1=[1,2,3]
print(l1[0:-1:1])
z=[1,2,3,4]
print(type(z))
t=(1,2,3)
print(type(t))
s={1,2,3}
print(type(s))
s=2
y=3
print(s//y)     #prints s//y
v={1,2,2,3}
print(type(v))
m=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
n=int(input())
type(n)
for i in range(n-1):
        for j in range(n):
            if ((i+j)==n-1):
                  print('/', end='')
            if(i==j):
                  print("\\", end='')
            else:
                print('*', end='')
        print()


    