# Функция apply_all_func принимает два параметра: int_list, который представляет собой список целых чисел и *functions,
# который позволяет передавать произвольное количество функций.

def  apply_all_func(int_list, *functions):
#  Создается пустой словарь results, где будут храниться результаты выполнения функций.
    results = {}
# Цикл проходит по каждой переданной функции в functions.
# Для каждой функции вызывается function(int_list), и результат сохраняется в словаре results с именем функции,
# доступным через function.name в качестве ключа.

    for function in functions:
        results[function.__name__]=function(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
