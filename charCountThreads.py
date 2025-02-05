import sys
import time
from multiprocessing import Process, Manager
from threading import Thread
def processFile(data, results):
    vovels = chars = spaces = punchs = 0

    for char in data:
        currentChar = ord(char)
        if (currentChar >= 97 and currentChar <= 122) or (currentChar >= 65 and currentChar <= 90):
            chars += 1
            if currentChar in (97, 101, 105, 111, 117):  # a, e, i, o, u
                vovels += 1
        elif currentChar == 32:
            spaces += 1
        elif currentChar in (33, 34, 39, 40, 41, 42, 44, 45, 46, 49, 58, 59, 60, 62, 63, 91, 93, 95):
            punchs += 1

    results.append((chars, spaces, punchs, vovels))

if __name__ == "__main__": 
    # Read file
    with open(sys.argv[1], 'r') as file:
        data = file.read()

    # Create partitions
    data1 = data[:len(data)//6]
    data2 = data[len(data)//6:len(data)//3]
    data3 = data[len(data)//3:len(data)//2]
    data4 = data[len(data)//2:len(data)*4//6]
    data5 = data[len(data)*4//6:len(data)*5//6]
    data6 = data[len(data)*5//6:]
    # data3 = data[]

    start = time.time()

    # Using multiprocessing
    with Manager() as manager:
        results = []

        p1 = Thread(target=processFile, args=(data1, results))
        p2 = Thread(target=processFile, args=(data2, results))
        p3 = Thread(target=processFile, args=(data3, results))
        p4 = Thread(target=processFile, args=(data4, results))
        

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()

        # Aggregate results
        total_chars = sum(r[0] for r in results)
        total_spaces = sum(r[1] for r in results)
        total_punchs = sum(r[2] for r in results)
        total_vovels = sum(r[3] for r in results)
        print(type(results), results)
        
        print("Total Characters:", total_chars)
        print("Spaces:", total_spaces)
        print("Punctuation:", total_punchs)
        print("Total length:", len(data))
        print("Characters (excluding spaces):", len(data) - total_spaces)
        print("Word Count:", total_spaces + 1)
        print("Vowels:", total_vovels)

    end = time.time()
    print("\nTime taken with multiprocessing:", end - start)
