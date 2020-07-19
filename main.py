# Importing Modules 
import convert
import binaryAdd
import numberValidation

# Boolean variables to for the continuity of the whole program and the Validity of the Data 
continueEntry=True
invalidData=False

# Introduction to the program
print("\n")
print("\t\t***** Welcome to the program *****")

# While Statement dor the continuity 
while continueEntry == True:
    # try and except to check the invalid data type
    try:
        
        #For First Number
        print("\n")
        firstNumber = int(input("\t Enter the first Number:  "))
        # Checking for the invalid data of the firstNumber
        invalidData=numberValidation.checkRange(firstNumber)

        # For the continuity of the program
        while invalidData == True:
            print("\n")
            firstNumber = int(input("\t Enter First Integer Number in the range of 0 to 255: "))
            invalidData=numberValidation.checkRange(firstNumber)

        # Converting the number to binary as all it is 
        firstBinaryNo=convert.decimalToBinary(firstNumber)

        
        #For Second Number
        print("\n")
        secondNumber = int(input("\t Enter the second Number: "))
        # Checking for the invalid data of the secondNumber
        invalidData=numberValidation.checkRange(secondNumber)

        # For the continuity of the program
        while invalidData == True:
            print("\n")
            secondNumber = int(input("\t Enter Second Integer Number in the range of 0 to 255: "))
            invalidData=numberValidation.checkRange(secondNumber)

        # Converting the number to binary as all it is 
        secondBinaryNo=convert.decimalToBinary(secondNumber)

    
    except:
        print("\n")
        print("\tInvalid Data Type")
        invalidData=True
        
    
    #For Binary Addition
    if invalidData==False: 
        additionOutput=binaryAdd.binaryAddition(firstBinaryNo,secondBinaryNo)
        # IF case is the the output is more than 8 bit operation 
        if (firstNumber+secondNumber)>255:
            print("\n")
            print("\t Sorry the sum of the two numbers is greater than 8 binary digits i.e. Maximum value")
        else:
            additionOutputInString=convert.listToString(additionOutput)
            additionOutputInDecimal=firstNumber + secondNumber
            print("\n")
            print("\t Binary Conversion of",firstNumber,"is \t:",convert.listToString(firstBinaryNo))
            print("\t Binary Conversion of",secondNumber,"is \t:",convert.listToString(secondBinaryNo))
            print("\t \t \t \t \t+-----------")
            print("\t Sum of Two Numbers is   \t:",additionOutputInString)
            print("\n")
            print("\t The Required Binary Addition is  :",int(additionOutputInString))
            print("\t The Required Decimal Addition is :",additionOutputInDecimal)

    #Input Statement to ask the user to continue the program
    print("\n")    
    entry = input("\t Do you want to run the Program?? 'Yes' or 'No' : ")
    if entry =="NO" or entry=="No" or entry=="no":
        continueEntry=False
        print("\n")
        print("\t\t***** Thank you for usig the program *****")
        print("\n")
        

