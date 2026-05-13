#DECORATOR

# DECORATOR EXAMPLE

def mainfunction(calculation):

    def display():
        print("The average value is ->")
        calculation()
    return display


@mainfunction
def calculation(a=55, b=33):
    print ((a + b) // 2)


calculation()
