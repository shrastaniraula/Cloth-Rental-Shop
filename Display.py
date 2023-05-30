def displaying():
    '''this method displays the items when display is called'''
    print("\n \nAll the details of the costumes\n")
    listShow() #caling listShow method for displaying the items
    print("\n \n")


def listShow():
    '''This method displays the items when called'''
    list_ = list() #assigning the value returned by list method to the variable 'list_'

    print("\n{:<25} {:<25} {:>1} {:>25} {:>35}\n".format("ID", "Name", "Brand", "Price", "Available quantity"))
    for one in list_:
        Id, name, brand, price, quan = one
        print("{:<17} {:<30} {:<27} {:<30} {:<10}".format(Id, name, brand, price, quan))


def list():
    '''this method stores the value from the textfile in a list which is further used for displaying'''
    file = open("costumes.txt", "r")
    list_ = []

    for lines in file:
        lines = lines.replace("\n", "")
        words = lines.split(",")
        list_.append((words[0:]))
    return list_
    
