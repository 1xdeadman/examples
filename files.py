file = open("Data/213.txt", "r")

print(file.read())
line = file.readline()
lines = file.readlines()
file.close()

with open("Data/213.txt", "r") as file:
    print(file.read())


file = open("Data/213.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

file = open("Data/213.txt", "r")
for line in file:
    print(line)
file.close()


with open("Data/text.txt", "w") as file:
    file.write("row1")
    file.writelines(["row2\n","row3\n"])
