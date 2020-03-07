import numpy as np

def get_predict(lower_bound,upper_bound):
    return int(lower_bound + upper_bound)//2

'''
The implementation of Division by 2 algorithms https://en.wikipedia.org/wiki/Division_by_two
The expected mean value 4 is explained easily even from elementary logic(or probability theory). What we have is :
1 (the best case)- the minimum number of attempts - if we identify settled number from the 1st attempt
7 (the worst case)- the maximum number of attempts (because of 2**7 = 128, which is estimation above of 100)
Thus on average (7+1)/2 = 4 - exactly the result we have  
'''
def game_core_v3(number,lower_bound,upper_bound):  

    count = 0
    predict = get_predict(lower_bound,upper_bound)
    while number != predict:
        count+=1
        if number > predict: 
            lower_bound = predict+1
        elif number < predict: 
            upper_bound = predict-1          
        predict = get_predict(lower_bound,upper_bound)                 
    return(count) 

def score_game(game_core):
    lower_bound = 1
    upper_bound = 101
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(lower_bound, upper_bound, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number,lower_bound,upper_bound))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v3)