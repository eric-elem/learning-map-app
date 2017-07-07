from __future__ import print_function


print("_______________________________________________")
print(" ")
print("Learning Map")
print(" ")

#user name
user_name = input("Enter Your Name: ") 
print("_______________________________________________ ")
print("Welcome " + user_name)  

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
    print("Added Skill")
elif option_input == 'b':
    print("view added")
elif option_input == 'c':
    print("view studied skill")
elif option_input == 'd':
    print("show learning progress")
else:
    print("Sorry Option Unvailable: :please input in letters e.g a")                

    
