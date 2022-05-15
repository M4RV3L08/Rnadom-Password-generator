###Author:M4RV3L_08
import os,random,string

os.system('cls')

user_options_choosed = []
pass_list = []
pass_len =''
symbols = "~!@#$%^&*()_-+={[}]|\:;<,>.?/"

path = "GeneratedPasswords.txt"
f = open(path,'a+')
f.readlines()



def option_choosing():
    ''' This method get options from user '''
    global pass_len

    pass_len = input("1.Password Length(atlest 8 character):") 
    if pass_len.isdigit() == True and int(pass_len) >= 8 :
        if int(pass_len) > 32 or int(pass_len) < 8:
            print("Invalid password length , defaultly 8 choosed for length")
            pass_len = '8'
    elif pass_len.isnumeric() == False  :
        print("Password length just colud be number! defaultly 8 choosed for length")
        pass_len = '8'
    elif int(pass_len) < 8 :
        print("Password lenght is too short , 8 defaultly choosed for lenght ")
        pass_len = '8'
         


    is_symbols = input("2.Include Symbols(Y / N):").lower() or 'y'
    if is_symbols in ['y','yes'] and is_symbols.isalpha() == True:
        user_options_choosed.append('is_symbols')
    elif is_symbols in ['n','no'] :
        pass
    else:
        print("Invalid input!! 'yes' defaultly used for this option")
        user_options_choosed.append('is_symbols')

    is_number = input("3.Include Numbers(Y / N):").lower() or 'y'
    if is_number in ['y','yes'] and is_number.isalpha() == True:
        user_options_choosed.append('is_number')
    elif is_number in ['n','no'] :
        pass
    else:
        print("Invalid input!! 'yes' defaultly used for this option")
        user_options_choosed.append('is_number')


    lower_case = input("4.Include Lowercase(Y / N):").lower() or 'y'
    if lower_case in ['y','yes'] and lower_case.isalpha() == True:
        user_options_choosed.append('lower_case')
    elif lower_case in ['n','no'] :
        pass
    else:
        print("Invalid input!! 'yes' defaultly used for this option")
        user_options_choosed.append('lower_case')
        

    uper_case = input("5.Include Uppercase(Y / N):").lower() or 'y'
    if uper_case in ['y','yes'] and uper_case.isalpha() == True:
        user_options_choosed.append('uper_case')
    elif uper_case in ['n','no'] :
        pass
    else:
        print("Invalid input!!'yes' defaultly used for this option")
        user_options_choosed.append('uper_case')


def main_func (options_list):
    global pass_list
    
    if len(user_options_choosed) > 0:
        for j in range(int(pass_len)):
            random_option = random.choice(options_list)
            if random_option == 'uper_case':
                pass_list.append (random.choice(string.ascii_uppercase))
            if random_option =='lower_case':
                pass_list.append(random.choice(string.ascii_lowercase))
            if random_option == 'is_number':
                pass_list.append(random.choice(string.digits))
            if random_option == 'is_symbols':
                pass_list.append(random.choice(symbols))
    else:        
        while True:
            if len(user_options_choosed ) == 0:
                print("You choosed no options for password")
                option_choosing()
            else:
                main_func(options_list)
                break

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
            user_options_choosed =[]
            option_choosing()
            main_func(user_options_choosed)
        else:
            main_func(user_options_choosed)
    else:
        
        break
pass_list_see =input("Do you wanna see last generated password?(Y / N):") or 'n'
f.close()
if pass_list_see == 'y':
    osCommandString = "notepad.exe E:/Python Test's/GeneratedPasswords.txt"
    os.system(osCommandString)
    print("   #GOOD_LUCK   \n  SEE YOU LATER  ")
else:
    print("   #GOOD_LUCK   \n  SEE YOU LATER  ")