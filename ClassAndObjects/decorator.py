def moderate(praveen):
    def high():
        print("How are You?")
        praveen()
        print("Where are you living?")
    return high
@moderate
def praveen():
    print("I am fine!")
praveen()