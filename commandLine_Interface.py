from __future__ import print_function

from src.task import Task

tasks = Task()

print("_______________________________________________")
print(" ")
print("Learning Map")
print(" ")

#user name
user_name = input("Enter Your Name: ") 
print("_______________________________________________ ")
print("Welcome " + user_name)  

while True:

    print(" ")
    print(" [a]- Add skill")
    print(" ")
    print(" [b]- View Added Skill")
    print(" ")
    print(" [c]- View Skills Studied")
    print(" ")
    print(" [d]- Show Learnin Progress")
    print("__________________________________________________")

    option_input = input("Enter Option: ")  #options
    print(" ")
    if option_input == 'a':
        ans = input("What would you like to learn? :")
        tasks.add_skill(ans)
    elif option_input == 'b':
        print(tasks.view_skills())
    elif option_input == 'c':
        print("view studied skill")
    elif option_input == 'd':
        print(tasks.progress_bar())
    else:
        print("Sorry Option Unvailable: :please input in letters e.g a")



    
