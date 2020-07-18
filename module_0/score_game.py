import game_core
import numpy as np
def score_game(game_core, number, rand_num_min, rand_num_max):
    #'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(rand_num_min,rand_num_max, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number, rand_num_min, rand_num_max))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))
    return(score)

    