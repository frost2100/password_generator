import random

#function for shuffling letters in password string

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList) #.join used to join iterable's elements

#start main program
#chr() function returns a string from a Unicode integer
uppercaseLetter1 = chr(random.randint(65, 90)) #Generates a random uppercase letter
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122)) # generates a random lowercase letter
lowercaseLetter2 = chr(random.randint(97, 122))
lowercaseLetter3 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57)) #generate a random number
digit2 = chr(random.randint(48, 57))
digit3 = chr(random.randint(48, 57))
punctuation1 = chr(random.randint(33, 152)) #generate a random puncuation
punctuation2 = chr(random.randint(33, 152))
punctuation3 = chr(random.randint(33, 152))

#generate password using all generated characters
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 +  lowercaseLetter3 + digit1 + digit2 + digit3 + punctuation1 + punctuation2 + punctuation3
password = shuffle(password)

print(password)