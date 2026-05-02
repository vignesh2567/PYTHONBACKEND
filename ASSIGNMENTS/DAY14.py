
#IF ELSE USING LAMBDA FUNCTION

username = input ("ENTER USER NAME: ")

un = lambda u : "APPROVED" if u == "vicky" else "INVALID!!!"

print (un(username))
