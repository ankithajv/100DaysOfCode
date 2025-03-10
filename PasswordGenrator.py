# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers=[1,2,3,4,5,6,7,8,9]
# symbols=["!", "#", "$", "?" "@"]
# import random
# lrt=int(input("How many letters you want in Password: "))
# sym=int(input("How many symbols you want in Password: "))
# num=int(input("How many numbers you want in Password: "))

# password=""
# let=""
# bols=""
# no=0

# for i in range(1,lrt+1):
#     let+=random.choice(letters)
# for i in range(1,num+1):
#     no+=random.randint(1,10)
# for i in range(1,sym+1):
#     bols+=random.choice(symbols)

# print("Your password is:"+ let +""+str(no)+""+bols)


#                         OR
#THIS WAS EASY VERSION
# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers=[1,2,3,4,5,6,7,8,9]
# symbols=["!", "#", "$", "?", "@"]
# import random
# lrt=int(input("How many letters you want in Password: "))
# sym=int(input("How many symbols you want in Password: "))
# num=int(input("How many numbers you want in Password: "))
# password=""

# for i in range(1,lrt+1):
#     password+=random.choice(letters)
# for i in range(1,num+1):
#     password+=str(random.choice(numbers))
# for i in range(1,sym+1):
#     password+=random.choice(symbols)

#     print(password)

#hard version!!!!!!!!!!!!!!!


letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1,2,3,4,5,6,7,8,9]
symbols=["!", "#", "$", "?", "@"]
import random
lrt=int(input("How many letters you want in Password: "))
sym=int(input("How many symbols you want in Password: "))
num=int(input("How many numbers you want in Password: "))
password=[]

for i in range(1,lrt+1):
    password.append(random.choice(letters))
for i in range(1,num+1):
    password.append(str(random.choice(numbers)))
for i in range(1,sym+1):
    password.append(random.choice(symbols))
random.shuffle(password)
# print(f"Generated password:"+"".join(password))

f_password = ""

for i in password:
    f_password+=i

print(f"Generated password:{f_password}")