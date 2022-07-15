from curses.ascii import islower


def Cesar (text, key):
    alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetLower = alphabetUpper.lower()
    encryptText = ''

    for l in text:
        if l == ' ':                # If letter == space
            encryptText += l        # Add space to the encrypt text
        
        else:
            if islower(l):          # If text is lower case

                index = alphabetLower.find(l) + key

                if index >= 26:
                    index = index - 26

                encryptText += alphabetLower[index]     # Find the letter in the lower alphabet
            

            else:                   # If text is upper case

                index = alphabetUpper.find(l) + key

                if index >= 26:
                    index = index - 26

                encryptText += alphabetUpper[index]     # Find the letter in the upper alphabet


    return encryptText