f = open('english3.txt', 'r')
f2 = open('nineletter', 'w')
for word in f:
    if len(word) == 10: #includes new line character /n
        f2.write(word)

f.close()
f2.close()

