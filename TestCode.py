import re

def stringSearcher(Answer):
    f = open("QuestionTree.txt", "r")
    currentLine = f.readline()
    for line in f:
        if re.match(Answer, line): 
            yesnos, answerOrQuestion = line.split(',')
            return answerOrQuestion, yesnos

while True:

    Answer = raw_input("Y or N: ")
    answerOrQuestion, yesnos = stringSearcher(Answer)
    if Answer == yesnos:
        print answerOrQuestion
        
