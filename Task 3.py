#Напишите функцию, которая принимает на вход строку, состояющую из символов '(' и ')', задающих скобочную последовательность, и возвращает True, если последовательность корректна, иначе False.
str = str(input('Введите строку '))

def trueOrFalse(str):
    counter = 0
    for i in str:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -=1
        if counter < 0:
            return False   
    return True
   
print(trueOrFalse(str))