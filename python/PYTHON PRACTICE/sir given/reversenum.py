n=int(input("enter the number:"))
sum=r=0
while n>0:
   r=n%10
   sum=sum*10+r
   n=n//10

print("the reversed number",sum)