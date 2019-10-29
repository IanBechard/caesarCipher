alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
LIST_LEN = len(alphaList)

#Encrypts string s, with key n
def encrypt(s, n):
    newstr = ""
    #loop through chars in string
    for x in s:
        #get current letters value and add key
        val = alphaList.index(x)
        val += n

        #make sure new value is still in bounds of alphaList
        while(val >= LIST_LEN):
            val -= LIST_LEN
        #add new letter to return string
        newstr += alphaList[val]

    return newstr

#Decrypts string s, with key n
def decrypt(s, n):
    newstr = ""
    #loop through chars in string
    for x in s:
        #get current letters value and add key
        val = alphaList.index(x)
        val -= n

        #make sure new value is still in bounds of alphaList
        while(val < 0):
            val += LIST_LEN
        #add new letter to return string
        newstr += alphaList[val]

    return newstr

#Main program loop, repeated as many times as user wishes
while(True):
    #Collect input info
    choice = input("Would you like to encrypt or decrypt? (e/d): ").lower()
    str = input("Please enter your string: ").lower()

    #Get acceptable num input, if num is 0 or divisible by LIST_LEN, the string will not be scrambled
    while(True):
        num = int(input("Please enter a key (positive integer): "))
        if((num%LIST_LEN != 0) and (num != 0)):
            break

    #Either encrypt or decrypt the string
    if(choice == "e"):
        print("Encrypted String: ", encrypt(str, num))
    elif(choice == "d"):
        print("Decrypted String: ", decrypt(str, num))
    else:
        print("Invalid input: aborting")
        break

    if(input("Would you like to quit? (y/n): ").lower() == "y"):
        break
