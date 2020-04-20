file = open("TestData/test", "r", encoding="utf-8")
# print(file.read())  # читать весь файл целиком
# print(file.read(2))  # читать 2 символа
symbols = file.read(2)
line = file.readline()  # считать строку файла (\n)
lines = file.readlines()  # считать весь файл построчно
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

with open("Data/text1.txt", "w") as file:
    file.write("row1")
    file.write("row1")
    file.write("row1\n")
    file.writelines(["row2\n", "row3\n"])

with open("Data/text2.txt", "a") as file:
    file.write("row1\n")
    file.write("row1\n")
    file.writelines(["row2\n", "row3\n"])
