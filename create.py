def Input(text):
    try:
        return input(text)
    except:
        print "Nice Try! Numbers only."
        return Input(text)
def create():
    try:
        numbers = raw_input("Please enter the numbers with a space seperating them: ")
        list = []
        for i in numbers.split(" "):
            list.append(int(i))
        return list
    except:
        return create()
    #amount = Input("How many numbers would you like to enter?\n - ")
    #list = []
    #print "Now please enter them:\n"
    #for i in range(amount):
    #    list.append(Input(" - "))
    #return list
