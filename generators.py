# learning python, 5th edition, chapter 20
# https://docs.python.org/3/glossary.html
# https://habr.com/ru/post/337314/


def my_pow_range(start, pow_count, pow=2):
    my_elem = start
    current_pow_count = 0
    while current_pow_count < pow_count:
        yield my_elem
        my_elem = my_elem ** pow
        current_pow_count += 1


print(my_pow_range(1, 10, 2))

for i in my_pow_range(2, 10, 2):
    print(i)


# print([x for x in my_pow_range(2,10,2)])
