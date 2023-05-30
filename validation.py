def rentIdCheck(list_):
    '''This method is to validate the id of costume while renting'''

    while True:
        costume = input("\nPlease enter the id of costume you want to rent.")
        IdCostume = 0
        available = False
        try:
            costume = int(costume)
            for each in list_:
                if(costume == int(each[0])):
                    available = True
                    IdCostume = costume
                    break

            if(available == False):
                print("\n\t\t*******\nSorry, this item is not available with us right now.\n\t\t*******\n")
                # rentIdCheck(list_)
            else:
                break
        except:
            print("\n\t\t*******\nPlease enter a valid numerical value\n\t\t*******\n")
            # rentIdCheck(list_)

    return IdCostume

def rentQuantityCheck(list_, costume):
    '''This method is to validate the quantity of the costume while renting'''

    while True:
        quantity = (input("How many quantities of this costume you want to rent?"))

        try:
            quantity = int(quantity)
            if(quantity <= int(list_[int(costume)-1][4])):
                if(quantity <= 0):
                    print("\n\t\t*******\nSorry, the quantity should be entered in positive value\n\t\t*******\n")
                    # rentQuantityCheck(list_, costume)
                else:
                    break
            elif(quantity > int(list_[int(costume)-1][4])):
                print("\n\t\t*******\nSorry we dont have this much quantity of the entered item.\n\t\t*******\n")
                # rentQuantityCheck(list_, costume)
            # else:
            #     break


        except:
            print("\n\t\t*******\nPlease enter a valid numerical value\n\t\t*******\n")
            # rentQuantityCheck(list_, costume)

    return quantity
    

def nameCheck(initial):
    '''This method is to validate all the names (last name, first name) of the costume while both renting and returning'''
    
    while True:
        takeName = input(f"\nPlease enter your {initial} name: ").upper().strip()
        if(takeName.isalpha() == False):
            print("\n\t\t*******\nPlease enter a valid Name and try again.\n\t\t*******\n")
            # nameCheck(initial)
        else:
            break
    
    return takeName


def billNoCheck():
    '''This method is to validate the bill no of the invoice asked while returning'''
    
    while True:
        try:
            value = int(input("Please enter the bill no provided to you while renting: "))
            value = str(value)
            break
        except:
            print("\n\t\t*******\nEnter a valid numerical value.\n\t\t*******\n")

    return value


