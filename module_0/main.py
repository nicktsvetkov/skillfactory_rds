import numpy as np
import score_game
import game_core
count = 0                            # счетчик попыток
print('Введите нижнюю границу диапазона (целое число), из которого будет генерироваться случайное число:')
rand_num_min = int(input())
rand_num_max = rand_num_min-1
while rand_num_min>rand_num_max:
    print('Введите верхнюю границу диапазона (целое число), из которого будет генерироваться случайное число (должно быть не меньше нижней границы):')
    rand_num_max = int(input())
number = np.random.randint(rand_num_min,rand_num_max+1)    # загадали число
print("Загадано число от {} до {}".format(rand_num_min, rand_num_max))
score_game.score_game(game_core.game_core_v5, number, rand_num_min, rand_num_max)

