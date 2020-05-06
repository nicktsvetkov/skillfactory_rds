def game_core_v3(number):
   # '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    #   Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    rand_min_score = rand_num_min
    rand_max_score = rand_num_max
    predict = np.random.randint(rand_min_score,rand_max_score)
    while number != predict:
        predict = np.random.randint(rand_min_score,rand_max_score)
        count+=1
        if number > predict: 
            rand_min_score = predict
        elif number < predict: 
            rand_max_score = predict
    return(count) # выход из цикла, если угадали