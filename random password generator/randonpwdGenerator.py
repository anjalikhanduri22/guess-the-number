import random
import string
charvalues=string.ascii_letters + string.digits + string.punctuation

print(charvalues)
limit=int(input("enter the password limit:"))
count=0
password=" "

while count<limit:
    password += random.choice(charvalues)
    
    count+=1
print("generated password is:",password)