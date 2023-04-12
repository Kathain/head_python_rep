a = int(input())
text = 'Even' if a % 2 == 0 else 'Odd'
print(text)


a, b = int(input()), int(input())
maximum, minimum = (a, b) if a > b else (b, a)
print(minimum, maximum)

print('Вопросительное' if input().endswith('?') else 'Обычное')


sentence = 'Вопросительное' if (input()[-1]) =='?' else 'Обычное'
print(sentence)


a1, b1 = input(), input()
experiment = 'Притягиваются' if a1 != b1 else 'Отталкиваются'
print(experiment)