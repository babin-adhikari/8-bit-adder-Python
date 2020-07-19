
def binaryAddition(a,b):
    # defining variables
    addition=[]
    actualBinary=[]
    c=[0,0,0,0,0,0,0,0]

    # d is the length of the List
    d=len(a)-1

    # Interation for a bit operation that takes Input values of index 
    for i in range(d+1):
        # Logical Operation of SUM and Carry
        sum = a[d-i] ^ b[d-i] ^ c[d-i]
        # Changing the value of the C List where index - 1
        c[(d-i)-1]= (c[d-i] and (a[d-i] ^ b[d-i])) or (a[d-i] and b[d-i])
        addition.append(sum)

    #The addition has the output of the binary additon in reverse format So we have to reverse the list
        
    for i in range(len(addition)-1,-1,-1):
        actualBinary.append(addition[i])
    return actualBinary

