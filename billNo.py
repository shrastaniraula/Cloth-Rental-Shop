from bill import out; 

def readValue():
        '''This method is to extract the value from the text file "bill.txt" '''

        file = open("bill.txt", "r")

        for lines in file:
                lines = lines.replace("\n", "").strip()
                # print(lines)
        
        return lines


def changeValue():
        '''This method is to increase the value in the text file "bill.txt" after generation of each invoice while renting.'''
        value = readValue()
        value = int(value)
        changedValue = value + 1
        with open("bill.txt", "w") as g:
                g.write(f"{changedValue}")

