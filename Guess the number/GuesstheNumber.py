import random
lower=int(input("enter the lower range:"))
upper=int(input("enter the upper range:"))
randm=random.randint(lower,upper)
count=0
max_try=10
print("you have total attempts:",max_try)

while count<max_try:
    userchoice=(input("enter the number or quit:"))
    
    if(userchoice=="quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==randm):
        print("success")
        count+=1
        break
    elif(userchoice < randm):
        print("your number is smaller,try again")
    else:
        print("your number is bigger,try again")
    count+=1
print("number of guess:",count)

print("---Game over---")