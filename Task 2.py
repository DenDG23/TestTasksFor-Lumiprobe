#Напишите функцию, которая на вход принимает единственное целое число N, а возвращает целый квадратный корень из этого числа, если такой существует, или None, если такого корня нет. Нельзя использовать функцию sqrt() из модуля math для извлечения квадратного корня.
#Правильная реализация, работает быстрее, если корня нет
def issqrt(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, int(n/2)):
        if i*i == n:
            return(i)
    return None


#Правильная реализация №2, избегает условий, как в предыдущей
def issqrt(n: int) -> int:
    for i in range(n + 1):
        if i*i == n:
            return(i)
    return None

#Реализация в обход правила (функцию sqrt() из модуля math не используется)
def issqrt(n: int) -> int:
    if n < 0:
        return None
    result = int(n**0.5)
    if n**0.5 == result:
        return result
    return None

print(issqrt(0))