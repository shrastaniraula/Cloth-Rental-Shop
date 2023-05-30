import Display
import dateNow
import validation
import billNo


def renting():  
    '''This method is to rent the costume and generate the invoice'''

    list_ = Display.list() #storing the list of details of costumes in 'list_'
    rentedCostumeList = []
    datee = dateNow.getDateTime() #calling 'getDateTime()' method from 'dateNow' class to get current date and time
    

    print("\nPlease have a look at the items you can rent:")
    Display.listShow()
    rentLoop = True

    #looping in order to ask the id and costume unless the user wants not to 
    while rentLoop== True:
        costume = str(validation.rentIdCheck(list_))
        quantity = validation.rentQuantityCheck(list_, costume)
        rentedCostumeList.append([costume, quantity])

        askLoop = True
        while askLoop == True:
            continue_ = input("\nDo you want to rent more items? (Y/N): ").upper()
            if continue_ == "Y":
                rentLoop = True
                askLoop = False
            elif continue_ == "N":
                rentLoop = False
                askLoop = False
            else:
                print("\n\t\t*****\nPlease enter a valid value. (Y/N)\n\t\t*****\n")
                askLoop = True

    #asking for the credentials before generating the invoice
    print("\nPlease enter your credentials for billing:")
    nameCustFirst = validation.nameCheck("first")
    nameCustLast = validation.nameCheck("last")
    address = input("Enter Customer address: ")
    contactNum = input("Enter contact Number of customer")
    nameCust = nameCustFirst + "-" + nameCustLast 
       


    #appending the values of details of rented items for generating invoice 
    billList2d = []
    GrandTotal = 0
    newlist = Display.list()
    
    for each in rentedCostumeList:
        costumeId, repeat = each
        for one in list_:
            Id, name, brand, price, quan = one
            if (Id == costumeId):
                bill = []
                price = int(price.replace("$", ""))
                quan = int(quan.strip())
                bill.append(name)
                bill.append(brand)
                bill.append(repeat)
                bill.append(price)
                priceTotal = (price * repeat)
                bill.append(priceTotal)
                bill.append(costumeId)
                billList2d.append(bill)

                GrandTotal = priceTotal+ GrandTotal
               
                Id = int(Id)
                newlist[Id- 1][4] = int(newlist[Id-1][4])- repeat
                update_quan_in_txt(newlist) #calling the method for upadating the text file after renting
    


    #generating the invoice
    value = str(billNo.readValue())
    invoiceName = value + "-" + nameCust
    with open(invoiceName.upper() + ".txt","w") as f:
        f.write("""<<<<<<-----------------------------------------RENTAL COSTUME SHOP----------------------------------------->>>>>>\n""")
        f.write(f"""----------------------------------------------DATE:{datee}--------------------------------------------\n\n""")
        f.write(f"Bill no: {value}")
        f.write(f"Name of Customer: {nameCustFirst} {nameCustLast}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Contact Number: {contactNum}\n\n")
        f.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        f.write("{:<33} {:<19} {:<12} {:<19} {:<19} {:<10}\n".format("Name", "Brand", "Quantity", "Price per unit", "Total Price","ID"))
        f.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        for each in billList2d:
                nameIV, brandIV, quantity, priceOfOne, total, ID = each
                f.write("{:<30} {:<25} {:<15} {:<15} {:<18} {:<10}\n".format(nameIV, brandIV, quantity, priceOfOne, total, ID))
        f.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        f.write(f"\n\nGrandTotal: {GrandTotal:>80}\n")
        f.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        f.write(f"""You have to return the item before 5 days otherwise a fine of $2 per day for every item will be added to your bill\n""")
        f.write("""--------------------------------ALso, you have to return all the items at the same day----------------------------\n""")
        f.write("""-----------------------------------------------------------------------------------------------------------------\n""")
        f.write("""-----------------------------------------Visit Us Again!! Thank You!!!-------------------------------------------\n""")

    billNo.changeValue()

    print("\n\t\t*****\nThank you for renting from us. Hope you Visit Us Again\nPlease ask for the invoice, You'll need it while returning.\n\t\t*****\n")



def update_quan_in_txt(newlist):
    '''This method is to update the text file after renting'''
    file = open("costumes.txt", "w")
    for each in newlist:
        file.write(
            str(each[0])+","+ str(each[1])+","+str(each[2])+","+str(each[3])+","+str(each[4])+"\n"
        )
    file.close()
