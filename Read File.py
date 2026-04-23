f = open("file.txt", "r")

print(f.read())
f.seek(0)

print(f.readline())
f.seek(0)

print(f.readlines())

f.close()