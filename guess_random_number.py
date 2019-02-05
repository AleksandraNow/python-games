user=int(input('Guess the number between 1 to 9: '  ))
while user >9 or user <1:
    user=int(input('enter valid number'))
print('You choice is: ' ,user)
import random
generate_number=random.randint(1,9)
print('computer choice is: ', generate_number)
if user==generate_number:
    print('you are lucky guy')

elif user> generate_number:
    print('Too high number!')
        
elif user <generate_number:
    print('Too low number!')