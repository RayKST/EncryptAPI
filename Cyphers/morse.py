morseAlphabet ={
    "A":    ".-",
    "B":	"-...",
    "C":	"-.-.",
    "D":	"-..",
    "E":	".",
    "F":	"..-.",
    "G":	"--.",
    "H":	"....",
    "I":	"..",
    "J":	".---",
    "K":	"-.-",
    "L":	".-..",
    "M":	"--",
    "N":	"-.",
    "O":	"---",
    "P":	".--.",
    "Q":	"--.-",
    "R":	".-.",
    "S":	"...",
    "T":	"-",
    "U":	"..-",
    "V":	"...-",
    "W":	".--",
    "X":	"-..-",
    "Y":	"-.--",
    "Z":	"--..",
    "0":	"-----",
    "1":	".----",
    "2":	"..---",
    "3":	"...--",
    "4":	"....-",
    "5":	".....",
    "6":	"-....",
    "7":	"--...",
    "8":	"---..",
    "9":	"----."
}

def Morse (text):
    encryptText = ''
    for l in text.upper():
        if l == ' ':                # If letter == space
            encryptText += "/"      # Add / to the encrypt text
        
        else:
            encryptText += morseAlphabet[l]     # Add the morse code from the right letter
        
        encryptText += " "          # at the end of each iteration add space to text     


    return encryptText