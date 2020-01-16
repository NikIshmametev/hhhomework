from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    i = 0
    while i < N:
        yield randint(1, 100)
        i += 1


# написать генераторное выражение, которое делает то же самое
random_int = [randint(1, 100) for _ in range(N)]


N = int(input('Введите N: '))

for x in gen(N):
    print(x)
print((x for x in gen(N)))

print(random_int)
