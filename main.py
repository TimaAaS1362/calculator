from os import system
def clear_screen():
    clear = system('cls')

num1 = round(int(input('Enter first number: ')))
num2 = round(int(input('Enter second number: ')))
operators = input('Choose operation: \n'
                  '1 - Multiplication \n'
                  '2 - Divide \n'
                  '3 - Subtraction \n'
                  '4 - Addition \n')
if(operators == '1'):
    clear_screen()
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif(operators == '2'):
    clear_screen()
    result = num1 // num2
    print(f'{num1} // {num2} = {result}')
elif(operators == '3'):
    clear_screen()
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif(operators == '4'):
    clear_screen
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
else:
    clear_screen
    print('ERROR')

