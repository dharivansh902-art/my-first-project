f = open("file.txt", "r")

f.seek(5)
print(f.read())

f.close()