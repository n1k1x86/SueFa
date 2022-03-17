from random import randint

running = True

var_answ = ['stone', 'snip', 'paper']

def chooseVarAnsw(var_answ): 
    print('Choose one of following answer: \n> 0: {}\n> 1: {}\n> 2: {}'.format(var_answ[0], var_answ[1], var_answ[2]))
    try:
        user_answ = int(input())
    except ValueError:
        print('> You entered wrong value! Try again!')
        user_answ = None
        return user_answ
    else:
        if user_answ < 0 or user_answ >= 3:
            print('Choose values in range (0 - 2)')
            user_answ = None
            return user_answ
        return user_answ


def continue_game():
    print('> Do you want to continue game ? \n> Yes/No')
    res = input()
    if res == 'Yes' or res == 'No':
        return res
    else:
        print('You chose wrong answer ! Choose again !')
        res = continue_game()
        return res


while running:

    choose_answ_AI = randint(0,2)
    choose_answ_usr = None
    
    while choose_answ_usr == None:
        choose_answ_usr = chooseVarAnsw(var_answ)

    user_answ = var_answ[choose_answ_usr]
    AI_answ = var_answ[choose_answ_AI]

    print('\n> User answer: {} \n> AI answer: {}'.format(user_answ, AI_answ))

    if choose_answ_usr == 0 and choose_answ_AI == 1:
        print('> User WIN!')
    elif choose_answ_usr == 0 and choose_answ_AI == 2:
        print('> AI WIN!')
    elif choose_answ_usr == 1 and choose_answ_AI == 2:
        print('> User WIN!')
    elif choose_answ_usr == 1 and choose_answ_AI == 0:
        print('> AI WIN!')
    elif choose_answ_usr == 2 and choose_answ_AI == 0:
        print('> User WIN!')
    elif choose_answ_usr == 2 and choose_answ_AI == 1:
        print('> AI WIN!')
    elif choose_answ_usr == choose_answ_AI:
        print('> You choose same answers ! Try again !')
        continue
    else:
        print('> There was happened something wrong! :( Let\'s try again !')
        continue
    
    res = continue_game()

    if res == 'Yes':
        running = True
    else:
        running = False





        


