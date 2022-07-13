import questions.question as q

def start():
    print("Welcome to Quiz")
    print("Please Select Topic\na)Computer\nb)networking\nc)operating system\n\n")
    topic = input("Select a,b or c: ")
    points = 0
    
    if topic == "a":
        questions = q.computerQ
    elif topic == "b":
        questions = q.networkQ
    elif topic == "c":
        questions = q.osQ
    else:
        print("Invalid input")
    
    for i in range(1,len(questions)+1):
        print("Question no: ",i,")",questions[i]["Q"],"?\n")
        print("Options:-")
        for j in range(4):
            print(j+1,") ",questions[i]["option"][j])
        ans = int(input("Select Correct Option ex(1,2,3,4): "))
        if(questions[i]["option"][ans-1] == questions[i]["ans"],"\n\n"):
            points += 10
        
    print("Quiz Over")
    print("You Got",points,"Points")

    print("\n\n\nCorrect Answers Are: ")
    for i in range(1,len(questions)+1):
        print("Q",i+1,")",questions[i]["Q"])
        print("Answer => ",questions[i]["ans"],"\n\n")

    
btn = 1
while(btn):
    finalOption = input("Select S for Start Quiz\nSelect E for Exit\n")
    if(finalOption == "S"):
        start()
    elif(finalOption == "E"):
        btn = 0
    else:
        print("Invalid Input")