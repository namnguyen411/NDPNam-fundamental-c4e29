from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]

    import calculator
    x = randint(1,10)
    y = randint(1,10)

    op = choice(["+", "-", "*", "/"])
    
    result = calculator.calculator(x , y, op)

    return_result = choice([result - 2, result - 1, result, result, result, result, result, result + 1, result +2, result,result,result,result,result,])
    
    return [x, y, op , return_result]
    # return [x, y, op, result] 


def check_answer(x, y, op, return_result, user_choice):
    import calculator
    result = calculator.calculator(x ,y, op)
    if return_result == result:
        if(user_choice == True):
            return True
        else:
            return False

    if return_result != result:
        if(user_choice == False):
            return True
        else:
            return False
    # pass
