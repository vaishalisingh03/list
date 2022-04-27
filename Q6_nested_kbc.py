Question_list=["what is the capital of india?",
"what is aur national fruit?",
"what is aur national bird"]
option=[["delhi","chennai","chandigarh","bhopal"],
["mango","apple","orange","grapes"],
["sparrow","peacock","crow","hen"]]
solution=[1,1,2]
option_list=[["1.delhi","4.bhopal"],["2.appele","1.mango"],["3.crow","2.peacock"]]
i=0
sum=0
count=0
while i<len(Question_list):
    print(Question_list[i])
    j=0
    k=1
    while j<=len(option):
        print(k,".",option[i][j])
        k+=1
        j+=1
    num=input("do you want to 50 50 life line")
    if num=="yes":
        print("50 50 life line")
        if count<1:
            print(option_list[i])
            num1=int(input("enter the number"))
            if num1==solution[i]:
                sum+=1000
                print("your answer is correct")
                print("you win Rs/-",sum)
            else:
                print("your answer is wrong")
                break
            count+=1
        else:
            print("you alredy use your life line")
            num2=int(input("enter the number"))
            if num2==solution[i]:
                print("your answer is right")
                sum+=2000
                print("you win Rs/-",sum)
            else:
                print("your answer is wrong")
                print("you win rs.",sum)
                break
    else:
        num3=int(input("enter the number"))
        if num3==solution[i]:
            print("right answer")
            sum+=2500
            print("you win rs/-",sum)
        else:
            print("no chance")
            print("your ans is wrong")
            print("you lose the game")
            break
    i+=1
