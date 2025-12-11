a="Abhijith Jayakumar"
b=20
c="Marian Engineering College"
d=8.58

print(f"Hi! I am {a},{b} currently studying in {c} with a CGPA of {d}")
print()

num=int(input())
if (num<0):
    print("Negative")
elif (num==0):
    print("Zero")
else:
    print("Positive")
print()

for i in range(1,21):
    print(i,end=" ")
print()
print()
i=20
while (i>0):
    print(i,end=" ")
    i-=1
print()


def is_even(n):
    if n%2==0:
        return True
    else:
        return False

print(is_even(8))
print(is_even(5))
print(is_even(1000))
print()

nums=[1,10,55,43,25]
print(sum(nums))
print(max(nums))
print(min(nums))

print()

dic={"math": 85, "ds": 90, "os": 88}
avg=sum(dic.values())/len(dic)
print(avg)