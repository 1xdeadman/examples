# learning python, 5th edition, chapter 20
# https://habr.com/ru/post/337314/
# https://docs.python.org/3/glossary.html
# https://docs.python.org/3/tutorial/classes.html#generators
# https://docs.python.org/3/tutorial/classes.html#generator-expressions
# https://docs.python.org/3/reference/datamodel.html#object.__iter__
# https://docs.python.org/3/reference/expressions.html#generator.__next__
# https://habr.com/ru/post/132554/
# https://www.youtube.com/watch?v=vn6bV6BYm7w
# https://www.youtube.com/watch?v=8cMMO8fks-k

# генераторы списков
list5 = [x for x in range(50)]

# выражения-генераторы
iterator = (x for x in range(10))
print(iterator)
for i in range(3):
    print(next(iterator))


# итераторы по списку
data = [11, 12, 13]
iterator = iter(data)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # бросит исключение, т.к. значения закончились


# функции-генераторы
def my_pow_range(start, pow_count, pow=2):
    my_elem = start
    current_pow_count = 0
    while current_pow_count < pow_count:
        yield my_elem
        my_elem = my_elem ** pow
        current_pow_count += 1


iterator = my_pow_range(2, 10, 2)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in my_pow_range(2, 10, 2):
    print(i)

iterator = (x for x in my_pow_range(2, 10, 2))
