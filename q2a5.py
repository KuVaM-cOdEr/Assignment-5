print("WElcome to Program")
lowerlim=int(input("Enter lower range limit:"))
upperlim=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lowerlim,upperlim+1):
    if(i%n==0):
        print(i)
