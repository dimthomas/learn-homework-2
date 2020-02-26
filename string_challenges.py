import collections

# Вывести последнюю букву в слове
word = 'Архангельск'
print('Последняя буква в слове "Архангельск" - "{}"'.format(word[-1]))


# Вывести количество букв "а" в слове "Архангельск"
word = 'Архангельск'

sum_glass_letter = 0
for glass_letter in word:
    if glass_letter.lower() == 'а':
        sum_glass_letter += 1
print('В слове "Архангельск" {} букв "а"'.format(sum_glass_letter))



# Вывести количество гласных букв в слове
word = 'Архангельск'

sum_glass_letters = 0
list1 = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for glass_letter in word:
    if glass_letter.lower() in list1:
        sum_glass_letters += 1
      
print('В слове "Архангельск" {} глассных букв'.format(sum_glass_letters))



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print('В предложении {} слова'.format(len(sentence.split())))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

avg_word  = len(sentence.replace(' ', '')) / len(sentence.split())
print(f'Усреднённая длина слова = {avg_word}')