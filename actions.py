import Display
import Rent
import Return

def Start():
    '''This is the start of the program. It displays the welcoming message'''
    print("""------------------------Welcome to the Costume Rental Shop----------------------------\n""")
    print("""-------------------------------A shop you can rely on---------------------------------\n""")

def actions():
    '''This function asks the user if they want to rent, return, display or exit the program'''
    print("\nHello, how can we help you?\nHave a look at the actions you can choose from:")
    print("\n1. Rent Costumes")
    print("\n2. Return Costumes")
    print("\n3. Display details of the Costumes")
    print("\n4. Exit")


global exit1 #initializing global variable for running loop

def askCustomer():
    '''This function allows the user to call other funtions hence allowing them to rent, return, display or exit'''
    exit1=False 
    while exit1 == False: #running the loop untill the user tells to terminate
        actions() #calling this method in order to ask the user for what to do
        try:
            option = int(input("\nPlease choose a number for the respective action: "))
        except:
            print("\n\t\t*******\nPlease enter a valid numerical value from the options.\n\t\t******\n")
            askCustomer()

        if option == 1:
            # import Rent
            exit1=rentCostume(exit1) #calls the method for renting

        elif option == 2:
            exit1 = returnCostume(exit1) #class the method for returning

        elif option == 3:
            exit1 = display(exit1) #calss method to display the items in the shop

        elif option == 4:
            print("""\n\t\t*******\nPlease visit us again. Have a good day\n\t\t*******\n""")
            exit1 = True #terminates the program after a short message as the user asked
             
        else:
            print("\n\t\t*******\nOops the number isn't from the options. Please enter again.\n\t\t******\n") 


def rentCostume(exit1):
    '''this is the method for renting the costume'''
    Rent.renting()
    askM(exit1)



def returnCostume(exit1):
    '''this is the method for returning the costume'''
    Return.returning()
    askM(exit1)



def display(exit1):
    '''This method displays all the costumes and details available in the shop'''
    Display.displaying()
    askM(exit1)#calling the method askM to ask if the user wants to terminate or continue with the program.



def askM(exit1):
    '''This method asks if the user wants to terminate the program after each actions i.e rent, return or display'''

    ask = input("Do you wish to Exit or Continue the program?? Press Y to continue and N to exit!! ").upper().strip()

    if ask == "Y":
      askCustomer()
    elif ask == "N":
      print("\n\t\t*******\nThank you for choosing us. Please visit again\n\t\t*******\n")
      exit1 = True
    else:
        print("\n\t\t*******\nEnter a valid value (Y/N).\n\t\t*******\n")
        askM(exit1)
    return exit1
    
    