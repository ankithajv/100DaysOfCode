print("Welcome! to pizza DELIVERIZZZ....")

size=input("What size of pizza do you want to order ,\n S , M or L\n S=120,M=160,L=200")
bill=0
if size=="S":
    print("Okay!!")
    bill=120
    pep = input("You need oregano(30rs): y or n: ")
    if pep =="y":
        print("HMMM!! yummy")
        print("What About Cheese:")
        bill+=30
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    else :
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    print(f"Bill={bill}")

elif size=="M":
    print("Okay!!")
    bill=160
    pep = input("You need oregano(30rs): y or n: ")
    if pep =="y":
        print("HMMM!! yummy")
        print("What About Cheese:")
        bill+=30
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    else :
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    print(f"Bill={bill}")

else :
    print("Okay!!")
    bill=200
    pep = input("You need oregano(30rs): y or n: ")
    if pep =="y":
        print("HMMM!! yummy")
        print("What About Cheese:")
        bill+=30
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    else :
        cheese=input("What About Cheese(20rs): y or n:")
        if cheese=="y":
            bill+=20
        else :
            print("OKAY!! LET US PREPARE")
    print(f"Bill={bill}")
