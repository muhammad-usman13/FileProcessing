import sys
import time

def processFile(data):
    # intial variables
    vovels = 0
    chars = 0
    spaces = 0
    punchs= 0

    for char in data:
        currentChar = ord(char)
        if (currentChar >= 97 and currentChar<=122 ) or (currentChar >= 65 and currentChar <=90):
            chars +=1
            if(currentChar == 97 or currentChar == 101 or currentChar == 105 or currentChar == 111 or currentChar == 117 ):
                vovels +=1
        elif(currentChar == 32):
            spaces +=1
        elif(currentChar == 33 or currentChar == 34 or currentChar ==39 or currentChar ==40 or currentChar == 41 or currentChar == 42 or currentChar == 44 or currentChar == 45 or currentChar == 46 or currentChar == 49 or currentChar == 58 or currentChar == 59 or currentChar == 60 or currentChar == 62 or currentChar == 63 or currentChar == 91 or currentChar == 93 or currentChar == 95):
            punchs += 1
        
    return {
        'vowels': vovels,
        'chars': chars,
        'spaces': spaces,
        'punchs': punchs,
    }

# read file
with open(sys.argv[1], 'r') as file:
    data = file.read()
start = time.time()
wholeFile = processFile(data)
print("total: ",wholeFile['chars'])
print("Spaces: ",wholeFile['spaces'])
print("Punctuation: ",wholeFile['punchs'])
print("total length: ", len(data))
print("Total Characters: ",len(data) - wholeFile['spaces'])
print('Word Count: ', wholeFile['spaces']+1)
print('Vowels: ', wholeFile['vowels'])
end = time.time()
print("\n\nTime taken: ", end-start,)

