yr=int(input("Enter the year"))
if(yr%400==0):
    print("Leap Year")
elif(yr%4==0 and yr%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
