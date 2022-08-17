#Напишите функцию, которая принимает на вход строку, состояющую из символов '(' и ')', задающих скобочную последовательность, и возвращает True, если последовательность корректна, иначе False.
def trueOrFalse(s: str) -> bool:
    counter = 0
    for i in s:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -=1
        if counter < 0:
            return False   
    return True
   
print(trueOrFalse(s))