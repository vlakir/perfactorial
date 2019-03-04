import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print('Привет!\nЯ маленькая и глупая программа perfact. Все, что я умею '
      '- это 100 тысяч раз подряд посчитать факториал от 200.\n'
      'Время, за которое я с этим справляюсь, дает приблизительное представление '
      'о производительности вашего процессора.\n[', end='', flush=True)
before_time = time.perf_counter()
for i in range(1, 100000):
    factorial(200)
    if i % 1000 == 0:
        print('.', end='', flush=True)
print(']', end='', flush=True)
after_time = time.perf_counter()
print('\nГотово!')
time.sleep(2)
print('На этот раз я справилась за %.2f секунд' % (after_time - before_time))
