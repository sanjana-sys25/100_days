import random
while True:
    x=random.randint(1,6)
    y=random.randint(1,6)
    print("the numbers on the dice are",x,y)
    d=input("do you want another roll? y/n")
    if d=='y':
        continue
    elif d=='n':
        break
    else:
        print("invalid response")