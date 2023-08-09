"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    #Указываем границы, с помощью которых будет сужать область поиска
    border_min = 1
    border_max = 101
    
    count = 0 #количество попыток
    
    predict = np.random.randint(1,101) #компьютер закадывает число

    while number != predict:

      count += 1

      if predict > number:
        border_max = predict #Меняем занчение верхней границы на загаданное число
        predict = round((border_min + border_max)/2) 
      else:
        border_min = predict #Меняем занчение нижней границы на загаданное число
        predict = round((border_min + border_max)/2)

      if (border_max - border_min) <2:
        break

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
