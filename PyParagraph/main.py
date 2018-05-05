import re
import os

'ask for user to input text file, then add .txt extension and open that file'
userfile = input("Which file would you like to open?   ")
sentenceCount = 0
words = 0
with open(userfile + ".txt", "r") as text:
    'iterate through each line of the file, construct wordArray out of each separate word'
    'get count of words from length of array'   
    for line in text:
        wordArray = line.split(" ") 
        wordCount = len(wordArray)
        'add up total number of words using wordCount range, then divide to calculate average letters'
        for i in range(0, wordCount):
            words += len(wordArray[i])
        lettercount = words/wordCount
        'split by punctuation to get sentence count, then divide by wordCount for sentence length'
        sentenceCount += len(re.split("(?<=[.!?]) +" , line))
        sentenceLength = wordCount/sentenceCount
'create a new txt file in Output folder and print results'
output = os.path.join("Output", userfile + ".txt")

newfile = open(output, "w")

newfile.write(f"{userfile} analysis:\n")
newfile.write(f"Approximate Word Count: {wordCount}\n")
newfile.write(f"Approximate Sentence Count: {sentenceCount}\n")
newfile.write(f"Average Letter count: {lettercount}\n")
newfile.write(f"Average Sentence Length: {sentenceLength}")

print(f"{userfile} analysis:\n")
print(f"Approximate Word Count: {wordCount}\n")
print(f"Approximate Sentence Count: {sentenceCount}\n")
print(f"Average Letter count: {lettercount}\n")
print(f"Average Sentence Length: {sentenceLength}")
newfile.close()        