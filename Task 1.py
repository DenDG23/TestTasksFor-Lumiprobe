from numpy import character

def my_count(letter: character, text: str) -> int:
    count = 0
    for i in text:
        if i == letter:
            count += 1
    return count

def test(text: str) -> tuple:
    max = 0
    letter = 'a'
    for i in text:
        # counter1 = text.count(i) # можно использовать встроенную функцию
        counter1 = my_count(i, text) # моя реализация
        if counter1 > max:
            max = counter1
            letter = i
    return (letter, max)

print(test("111111"))
