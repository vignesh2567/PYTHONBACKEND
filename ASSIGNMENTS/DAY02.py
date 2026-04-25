# in operator

squad = "Rutu Samson Dube Ayush Sarfras"

player=input("search the player :")

if player in squad:
    print("HE IS PLAYING TODAY")
else:
    print ("HE IS NOT AVAILABLE")
    
    
# not in

installed_apps = "insta whatsapp X youtube"

app=input("Search the app :")

if app not in installed_apps:
    print ("App is not installed yet !")
else:
    print ("App is availabe")


# and operator

name = input("Enter your name :")

Id =int(input("Enter valid ID :"))

if name == "vicky" and Id == 33:
    print("Logged in successfully")
else:
    print ("invalid credential!")


# or operator

Degree=input("Enter your Degree: ")

if Degree == "BCA" or Degree == "Bsc":
    print("You can do MCA or Msc")
else:
    print ("You can't do both MCA and Msc")
