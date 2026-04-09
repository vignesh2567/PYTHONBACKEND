
#LADDER IF ELSE

point = int(input ("ENTER YOUR POINT :"))

if point > 20:
    print("Enter a valid point")
elif point == 20:
    print ("QUALIFIED")
elif point < 20 and point >= 14:
    print("Can get QUALIFIED as a 2nd,3rd,4th TEAM")
elif point <14 and point >= 10:
    print("HARD to QUALIFY")
else:
    print("YOU CAN'T QUALIF THIS SEASON")


# NESTED IF ELSE

spec1 = int(input("Enter your RAM size :"))


if spec1 >= 16:

    spec2 = input("INTEL 5  OR AMD INTEL 7")
    if spec2 == "INTEL 7":
        print("YOU CAN DOWNLOAD THE GAME")
    else:
        print("Not having required processor")
else:
    print ("the game is not your device")
