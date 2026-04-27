#can open files in different types, read("r"), write("w"), append("a")

print("\nReading data.txt")
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
#opening a fle with 'r' will read and print whatever is already in the file

print("\nWriting with 'w' in data.txt ")
file = open("data.txt", "w")
file.write("\nTesting write in data file")
file.close()
#opening a file with 'w' will write to the file as if nothing had been written before

print("\nAdding writing with 'a' in data.txt\n ")
file = open("data.txt", "a")
file.write("\nTesting add write in data file")
file.close()
#opening a file with 'a' will add a write to the file

with open("data.txt", "r") as file:
    cont = file.read()
    print(cont)
#upon exiting the "with" block, the file opening is automatically terminated.
