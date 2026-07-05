# n = int(input("Enter a no: "))

# results = [str(n * i) for i in range(1, 11)]
# print(' '.join(results))s = "Geeks"
 

s = "Geeks"
words = s.split()
for word in words[0:5:2]:
    print(word)
