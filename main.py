print("QUIZ GAME ")

playing = input("Do you want to play the Game: " )

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play : ")
score = 0

answer = input("What does CPU stand for ? ")
if answer.lower()=="central processing unit":
    print("Correct Answer")
    score+=1
else :
    print("Incorrect")

answer = input("What does GPU stand for ? ")
if answer.lower()=="graphics processing unit":
    print("Correct Answer")
    score+=1
else :
    print("Incorrect")

answer = input("What does RAM stand for ? ")
if answer.lower()=="random access memory":
    print("Correct Answer")
    score+=1
else :
    print("Incorrect")


answer = input("What does PSU stand for ? ")
if answer.lower()=="power supply":
    print("Correct Answer")
    score+=1
else :
    print("Incorrect")

print(f"You got {score} score out of 4")
print(f"Your percentage is {(score/4)*100}%")

