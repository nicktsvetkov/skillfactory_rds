def game_core_v5(number):
   # '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    #   Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    rand_min_score = rand_num_min
    rand_max_score = rand_num_max
    predict = (rand_max_score - rand_min_score)/2
    while number != predict:
        if number > predict: 
            rand_min_score = (predict)
        elif number < predict: 
            rand_max_score = (predict)
        predict = int((rand_max_score+rand_min_score)/2)
        count+=1
    return(count) # выход из цикла, если угадали