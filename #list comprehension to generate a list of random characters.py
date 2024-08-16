#list comprehension to generate a list of random characters
import random
import string

n=int(input("Enter the length of the password: "))

pass_length=n
charValues=string.ascii_letters + string.digits + string.punctuation


password="".join([random.choice(charValues) for i in range(pass_length)])

print("Generated Password: ", password)