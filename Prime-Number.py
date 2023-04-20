x = int(input("Enter a number:\n"))
count = 0

for i in range(1, x+1):
    if(x%i == 0):
        count += 1
        
if(count == 2):
    print("Prime Number")
else:
    print("Not Prime Number")