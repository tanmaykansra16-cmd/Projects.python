print("Welcome to Python Pizza Deliveries!")
bill =0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
     bill = 15
elif size =="M":
     bill = 20
elif size =="L":
     bill = 25
else:
    print("you typed the wrong input")

wantPep=input("do you want pepperoni on your pizza? Y or N")
if wantPep == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
wantCheese= input("Do you want cheese on your pizza? Y or N")
if wantCheese == "Y":
    if size =="S":
        bill+=1

print(f"Your final bill is: ${bill}.")

























