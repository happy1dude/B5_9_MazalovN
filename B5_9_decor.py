import time
# Принимаем количество запусков
def time_this(num_runs = 10):
    #Принимает обертываемую функцию
    def decorator(func):
        # Создаём функцию обертку
        def wrap(): #
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func() # Обертывавемая функция
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        # Возвращаем обёртку
        return wrap
    # Возвращаем декоратор
    return decorator
# когда мы вызываем функию time_this(num_runs=10) она возвращает функцию decorator
# В итоге строчка ниже обозначает то же самое, что @decorator ,но с заданным количеством запусков
@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass
# Если хотим использовать количество запусков по умолчанию пишем @time_this()
f()