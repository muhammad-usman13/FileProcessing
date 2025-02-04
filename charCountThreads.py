import sys
import time
from threading import Thread

vovels = 0
chars = 0
spaces = 0
punchs= 0
def processFile(data):
    # intial variables
    global vovels, chars, spaces, punchs

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
        
    
    

# read file
with open(sys.argv[1], 'r') as file:
    data = file.read()

# creating Partitions
data1 = data[0:len(data)//2]
data2 = data[len(data)//2+1:len(data)]

start = time.time()

# creating threads
t1 = Thread(target=processFile, args=(data1,))
t2 = Thread(target=processFile, args=(data2,))
t1.start()
t2.start()

# get the returning values from threads
part1 = t1.join()
part2 = t2.join()

print("total: ",chars)
print("Spaces: ",spaces)
print("Punctuation: ",punchs)
print("total length: ", len(data))
print("Total Characters: ",len(data) - spaces)
print('Word Count: ', spaces+1)

end = time.time()

print ("\n\nTime taken for threads: ", end-start)
