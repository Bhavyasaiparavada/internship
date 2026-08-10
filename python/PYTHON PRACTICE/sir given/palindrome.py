n=int(input("enter the number:"))
r=0
sum=0
num=n
while n>0:
 r=n%10   
 sum=sum*10+r
 n=n//10

if num==sum:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")



