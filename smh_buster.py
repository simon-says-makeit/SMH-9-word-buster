import collections

def wordArray():
    f = open('nineletter', 'r')
    listOfWords = []
    for word in f:
        charWord = list(word.rstrip('\n'))
        listOfWords.append(charWord)
    f.close()
    return listOfWords

wordList = wordArray()
letters = input('please enter the 9 letters:')

chosenLetters = []
for i in range(0, len(letters)):
    chosenLetters.append(letters[i])

letterFrequency = collections.Counter(chosenLetters)

answers = []
for word in wordList:
    if letterFrequency == collections.Counter(word):
        print(''.join(word))
        





