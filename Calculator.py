print("Welcome to Sitybabu Calculator")
while 1:
    print("What would you like to do:")
    print("type 1 for addition")
    print("type 2 for substraction")
    print("type 3 for Multiplication")
    print("type 4 for division")
    print("type 5 for exit")
    user_choice = int(input("Enter your choice:"))
    if user_choice == 1:
        first_num = int(input("enter your 1st number:"))
        second_num =int(input("enter your 2nd number"))
        print("output", first_num+second_num)
    elif user_choice == 2:
        first_num = int(input("enter your 1st number:"))
        second_num = int(input("enter your 2nd number:"))
        print("output", first_num-second_num)
    elif user_choice == 3:
        first_num = int(input("enter your 1st number:"))
        second_num = int(input("enter your 2nd number:")) 
        print("output", first_num*second_num)
    elif user_choice == 4:
        first_num = int(input("enter your 1st number:"))
        second_num = int(input("enter your 2nd number:")) 
        print("output", first_num/second_num)
    elif user_choice == 5:
        print("Exiting...") 
        break
    print()