# Function to change Decimal Number To Binary Number    
def decimalToBinary(number):
    # Initializing Variables
    bit=[]
    counter=0
    actualBinary=[]

    #Setting counter != 8 so that the binary number be of 8 digits
    while counter!=8:
        remainder=number%2
        bit.append(remainder)
        number=number//2 #Quotient linxa
        counter+=1

    # Reversing the List bit to get the required Binary Output
    for i in range(len(bit)-1,-1,-1):
        actualBinary.append(bit[i])
    return actualBinary

# Function to change the List to String
def listToString(List):
    actualNumber=""
    for i in range(len(List)):
        actualNumber=actualNumber+str(List[i])
    # Returning the int value of the String so that only the true addition is Displayed
    return actualNumber
