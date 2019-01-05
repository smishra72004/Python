# Hurdle 1
##############################################################
# Initializing Variables

userInput = ''
totalInputs = []
num = []
avg = 0

##############################################################
#Author: Simoni MIshra
#Date Created: 10/7/2018

##############################################################

##############################################################
# Input until STOP

while userInput != "STOP":
    userInput = input("?  ")
    totalInputs.append(userInput)

# Checking if num
#Test Case1: Validate if alphaneumeric and handle accordingly - Works
#Test Case2: Validate When Special character entered and handle accordingly
#Test Case3: Validate When space is entered as a value entered and handle accordingly
#Test Case4: Validate When single quote and double quote is entered with the value and handle accordingly



for eachPass in range(len(totalInputs)):
    isalpha = 0
    isnum = 0
    ischar = 0
    
    numVal = totalInputs[eachPass]
    numVal = numVal.replace(' ','')
        
    if numVal.isalpha() == False and numVal != '':
        for i in range(len(numVal)):
            
            if numVal[i].isalpha() == True:
                isalpha += 1
            elif numVal[i].isnumeric() == True:
                isnum += 1
            elif (numVal[i] != '.' and numVal[i] != '-') and numVal[i].isalpha() == False and numVal[i].isnumeric() == False:
                ischar += 1

        if not(isalpha > 0 and isnum > 0) and ischar == 0:
            print(numVal)
            if str(numVal)[:1] == '-':
                number = str(numVal).replace(numVal[:1], '')
                if number.isnumeric() == True or str(float(number)) == number:
                    num.append(float(numVal))

            # Checking if num    
            elif str(numVal).isnumeric() == True:
                num.append(float(str(numVal)))
                print('num')

            # Checking if float
            elif str(float(numVal)) == numVal and numVal[:1] != '-':
                num.append(float(numVal))
                
            elif float(numVal) == numVal and numVal[:1] != '-':
                num.append(float(numVal))
                print('hello')
                
            print(num)

##############################################################
# Output

if len(num) == 0:
    print("-1")
else:
    avg = sum(num)/len(num)
    print(avg)

        

