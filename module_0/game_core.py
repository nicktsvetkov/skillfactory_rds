
#  Алгоритм деления пополам (в качестве варианта ставим середину интервала, затем уменьшаем интвервал в половину в соответствующую сторону и повторяем)

def game_core_v5(number, rand_num_min, rand_num_max):
    #   Важно округлять в меньшую сторону новый вариант
    #   Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    rand_min_score = rand_num_min
    rand_max_score = rand_num_max
    predict = (rand_max_score - rand_min_score)/2
    while number != predict:
        if number > predict: 
            rand_min_score = (predict+1)
        elif number < predict: 
            rand_max_score = (predict-1)
        predict = int((rand_max_score+rand_min_score)/2)
        count+=1
    return(count) # выход из цикла, если угадали