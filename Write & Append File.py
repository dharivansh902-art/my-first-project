f = open("file.txt", "w")
f.write("Hello\n")
f.close()

f = open("file.txt", "a")
f.write("Append line")
f.close()