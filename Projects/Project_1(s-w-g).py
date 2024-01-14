import random
#Snake Water Gun

def gameWIN(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you=='w':
            return False
    elif you == 'g':
        return True
    
    elif comp == 'w':
        if you=='g':
            return False
    elif you == 's':
        return True
    
    elif comp == 'g':
        if you=='w':
            return False
    elif you == 's':
        return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNum = random.randint(1, 3)

if randNum == 1:
    comp = 's'
elif randNum ==2:
    comp = 'w'
elif randNum ==3:
    comp = 'g'

you = input("Your's Turn: Snake(s) Water(w) or Gun(g)?\n")

a = gameWIN(comp,you)

print(f"Comp choose {comp}")
print(f"You choose {you}")

if a== None:
    print("The game is tie!")
elif a:
    print("You WIN!")
else:
    print("You LOOSE!")