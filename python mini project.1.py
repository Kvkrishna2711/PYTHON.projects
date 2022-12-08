q1 = """"a"+"bc"=ac?"
a.True
b.False"""
q2 =""""Python is a dynamically typed language?"
a.True
b.False"""
q3=""""9 is the output of 3*1**3?"
a.True
b.False"""
q4=""""eval is not a keyword in python?"
a.True
b.False"""
q5=""""Is Python case Sensitive when dealing with Identifiers?"
a.True
b.False"""

questions = {q1:"False",q2:"True",q3:"False",q4:"True",q5:"True"}
name=input("Enter your Name: ")
print("Hello",name,"Welcome to the Quiz World")
score = 0
s =int(1)
for i in questions:
    print(s ,".", i)
    s = s + 1
    ans=input("Enter the Answer (True/False):")
    if ans==questions[i]:
        print("Correct Answer,You got 1 Point")
        score=score+1
    else:
        print("Wrong Answer,Try Next Question!!")
print("Final Score:",score)
