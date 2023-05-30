import validation
import Display
import datetime


def returning():
    '''this method is for returning the costumes that has already been rented ang generating invoice'''

    lineList = []
    totalPrice = 0
    newList = Display.list()
    value = "0"


    while True:
        #iterating the loop until the user inputs valid name and bill id for returning
        try:
            nameReturnFirst = validation.nameCheck("first")
            nameReturnLast = validation.nameCheck("last")
            value = validation.billNoCheck()

            nameReturn = value + "-" + nameReturnFirst + "-" + nameReturnLast

            file = open(nameReturn + ".txt", "r") #opening the invoice for the user that has come to return
            break
        except:
            print("\n\t\t*******\nSorry we dont have the data of you renting, please rent first or try again\n\t\t*******\n")


    #storing the lines of the invoice in a list
    for lines in file:
        lines= lines.strip()
        lineList.append(lines)


    date1 = 0 #initializing in order to prevent UnBoundLocalError

    dates = lineList[1].split("DATE:")
    actualDate = dates[1].split("-")
    rentYear, rentMonth, rentDay = map(int, [actualDate[0], actualDate[1], actualDate[2]])
    intoDate = datetime.date(rentYear, rentMonth, rentDay)
    

    #checking returning date
    while True:
        try:
            date_entry = input("Enter today's date(date of return) in YYYY-MM-DD format: ")
            year, month, day = map(int, date_entry.split("-"))
            date1 = datetime.date(year, month, day)
            break

        except:
            print("\n\t\t*****\nThe date you've entered is invalid. Please enter a valid date.\n\t\t*****\n")
            

    
    diff = date1 - intoDate #calculating the difference between rent date and return date
    datDiff = int(diff.total_seconds() / 86400) #convering the difference into days (int)
    

    
    #printing the items that was rented
    print("\n\nThe items that you rented are:")
    print(lineList[8])
    returnList = []
    for i in range(10,20):
        if (lineList[i] == "-----------------------------------------------------------------------------------------------------------------"):
            #iterates the list upto the lines where the items are written
            break


        print(lineList[i]) #displaying the lines of invoice
        okay = lineList[i].split("        ")#removing unawanted spaces from the calues
        okay1 = []
        for each in okay:
            add = each.strip()
            if(len(add) != 0): #excluding the unwanted null elements
                okay1.append(add) #appending the list of details given in invoice in a 1D list
        returnList.append(okay1) #appending the list of details given in invoice in a 2D list

        totalPrice = totalPrice + int(okay1[4])

        retQuan= int(okay1[2])
        retId = int(okay1[5])
        newList[retId-1][4] = int(newList[retId-1][4]) + int(retQuan)
        update_quan_in_txt(newList)#calling the method for updating the text file
            
    fee = 0
    if (datDiff > 5):
        #displaying total cost in console
        fee = (datDiff - 5) * 2
        print(f"\nYou are late to return the costume by {datDiff-5} days so your extra cost becomes {fee}")

    print(f"Your total cost to be paid is {totalPrice + fee}")
    print("\n\t\t*****\nThank you for renting. Please check your invoice.\n\t\t*****\n")


    #generating the invoice for returning
    with open("Return-" +nameReturn + ".txt", "w") as file:
        file.write("""<<<<<<-----------------------------------------RENTAL COSTUME SHOP----------------------------------------->>>>>>\n""")
        file.write(f"""------------------------------------------------DATE:{date1}----------------------------------------------------\n\n""")
        file.write(f"Name of Customer: {nameReturnFirst} {nameReturnLast}\n")
        file.write(f"""Date of Rent: {intoDate}\n""")
        file.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        file.write("{:<33} {:<19} {:<12} {:<19} {:<19} {:<10}\n".format("Name", "Brand", "Quantity", "Price per unit", "Total Price","ID"))
        file.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        for each in returnList:
                nameIV, brandIV, quantity, priceOfOne, total, ID = each
                file.write("{:<30} {:<25} {:<15} {:<15} {:<18} {:<10}\n".format(nameIV, brandIV, quantity, priceOfOne, total, ID))
        file.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        if(datDiff > 5):
            file.write(f"""Note: You are late to return the costume by {datDiff-5} days so your extra cost becomes ${fee}\n""")
            file.write(f"\n\nGrandTotal: {(totalPrice +fee):>80}\n")
        else:
            file.write(f"\n\nGrandTotal: {totalPrice :>80}\n")
        file.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        file.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        file.write("""-----------------------------------------Visit Us Again!! Thank You!!!-------------------------------------------\n""")




def update_quan_in_txt(newlist):
    '''This method is to update the text file after renting'''

    file = open("costumes.txt", "w")
    for each in newlist:
        file.write(
            str(each[0])+","+ str(each[1])+","+str(each[2])+","+str(each[3])+","+str(each[4])+"\n"
        )
    file.close()
