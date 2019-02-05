print('Winning rules of the rock, paper, scissors as follows: \n'
                                +'Rock vs Paper---> Paper wins!\n'
                                +'Rock vs scissors--->Rock wins!\n'
                                +'Paper vs scissors---> Scissors wins!')
while True:
    print('Enter choice\n 1.Rock \n 2.Paper \n 3.Scissors')
   
    choice_user =int(input('choose favorite number'))
    while choice_user>3 or choice_user<1: 
        choice_user=int(input('Enter valid number'))
    

     
    if choice_user == 1:
        choice_user_name= 'Rock'
    elif choice_user == 2:
        choice_user_name= 'Paper'
    elif choice_user == 3:
        choice_user_name= 'Scissors' 
    print( 'User turns ', choice_user)
    print('Now computer turns......')
    import random
    computer_choice=random.randint(1,3)
    
    while computer_choice== choice_user:
        computer_choice= random.randint(1,3)
    if computer_choice== 1:
        computer_choice_name= 'Rock'
    elif computer_choice == 2:
        computer_choice_name= 'Paper'
    else:
        computer_choice_name= 'Scissors'
    print('computer choice is ', computer_choice_name)
    print( choice_user_name , 'vs' ,computer_choice_name)


    if (choice_user == 1 and computer_choice== 2)  :
        print('Paper wins==> ', end='')
        result_1 ='paper'
    elif  (choice_user== 2 and computer_choice== 1 or choice_user == 3 and computer_choice== 2 or choice_user == 1 and computer_choice == 3):
        print('User wins')

    
    elif (choice_user == 1 and computer_choice == 2 or choice_user == 3 and computer_choice== 1 or choice_user== 3 and computer_choice== 2 ):
        print('Computer wins!')
  


    answer=input('Do you want to play again?\n')
    if answer== 'no' or answer== 'No' or answer== 'n' :
        print('Thanks for playing')
    break