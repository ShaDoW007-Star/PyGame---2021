# ---------------------------------------------Rock, Paper, Scissors---------------------------------------------------
import random


class a:
    cp = 0
    up = 0

    def game(self):
        l = int(5)
        global cp
        global up
        l = 5
        cp = 0
        up = 0
        while l > 0:
            x = ["r", "p", "s"]
            print("R for Rock")
            print("P for Paper")
            print("S for Scissors")
            u = input("Enter Your Choice : ")
            c = random.choice(x)
            if u == "r" and c == "p":
                cp = cp + 1
                print("Computer is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "p" and c == "s":
                cp = cp + 1
                print("Computer is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "s" and c == "r":
                cp = cp + 1
                print("Computer is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "r" and c == "s":
                up = up + 1
                print("User is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "s" and c == "p":
                up = up + 1
                print("User is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "p" and c == "r":
                up = up + 1
                print("User is Win...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "s" and c == "s":
                print("Tie...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "r" and c == "r":
                print("Tie...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            elif u == "p" and c == "p":
                print("Tie...!!!")
                print(f"Your Point {up} and Computer Point {cp}")
                l -= 1
                print(f"{l} Life Are There...")
            else:
                print("You Have Wrong Input...!!!")


def s():
    print(f"User Point {up} And Computer Point {cp} ")
    if up > cp:
        print("User Is Winner...")
    elif up == cp:
        print("Match is Tie")
    else:
        print("Computer Is Winner...")


b = a()
b.game()
s()
p = input("Do You Want To Play Again[Y/N]?")
while p != "n":
    if p == "y":
        b.game()
        s()
        p = input("Do You Want To Play Again[Y/N]?")
        if p == "n":
            break


