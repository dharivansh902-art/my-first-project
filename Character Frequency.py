s = input("Enter string: ")
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)