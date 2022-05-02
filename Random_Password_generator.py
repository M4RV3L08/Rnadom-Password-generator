import os,random

os.system('cls')

user_options_choosed = []
pass_list = []
pass_len =''
path = "GeneratedPasswords.txt"
f = open(path,'a+')
f.readlines()


uper_case_elements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case_elements = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = "~!@#$%^&*()_-+={[}]|\:;<,>.?/"

def option_choosing():

    while True:
        global pass_len
        pass_len = input("1.Password Lengh(atlest 6 charaacter):")
        if pass_len.isnumeric() == True:
            break
        else:
            print("password lengh just colud be number !!")
    is_symbols = input("2.Include Symbols(Y / N):").lower() or 'y'
    if is_symbols == 'y':
        user_options_choosed.append('is_symbols')

    is_number = input("3.Include Numbers(Y / N):").lower() or 'y'
    if is_number == 'y':
        user_options_choosed.append('is_number')
    lower_case = input("4.Include Lowercase(Y / N):").lower() or 'y'
    if lower_case == 'y':
        user_options_choosed.append('lower_case')
    uper_case = input("5.Include Uppercase(Y / N):").lower() or 'y'
    if uper_case == 'y':
        user_options_choosed.append('uper_case')

def upper_case_choocer():
    pass_list.append (random.choice(uper_case_elements))

def lower_case_choocer():
    pass_list.append(random.choice(lower_case_elements))
    
def number_choocer():
    pass_list.append(random.choice(numbers))

def symbol_choocer():
    pass_list.append(random.choice(symbols))


def main_func (options_list):
    global pass_list
    
    for j in range(int(pass_len)):
        random_option = random.choice(options_list)
        if random_option == 'uper_case':
            upper_case_choocer()
        if random_option =='lower_case':
            lower_case_choocer()
        if random_option == 'is_number':
            number_choocer()
        if random_option == 'is_symbols':
            symbol_choocer()

       
    final_password =''
    for i in pass_list:
        final_password += i
    pass_list =[] 
    print(f'your Password is : {final_password}')
    f.write('\n')
    f.write(final_password)
    


#START


print(" */|\* ~~~ RANDOM PASSWORD GENERATOR ~~~ */|\* \nPlease choose your password options \n")
option_choosing()
main_func(user_options_choosed)

while True:
    
    countinie = input("DO you wanna another password?(Y / N):").lower() or 'n'
    if countinie == 'y':
        pass_with_same_options = input("do you want to your new password be with privious options?(Y / N):").lower() or 'y'
        if pass_with_same_options == 'n':
            option_choosing()
    
            main_func(user_options_choosed)
        else:
            main_func(user_options_choosed)
    else:
        break
pass_list_see =input("Do you wanna see last generated password?(Y / N):") or 'n'
f.close()
print("   #GOOD_LUCK   \n  SEE YOU LATER  ")
if pass_list_see == 'y':
    osCommandString = "notepad.exe E:/Python Test's/GeneratedPasswords.txt"
    os.system(osCommandString)