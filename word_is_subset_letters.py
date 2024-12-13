"""
Алгоритм выбирает из текста такие слова, которые целиком состоят из указанных букв.
'word_is_subset_letters' / 'слово_является_подмножеством_букв'
"""
#
# Знаки, которые будем игнорировать.
delimiter_chars = [';', ':', '\'', '"', ',', '.', '?', '!', '-', ' ', '\n']
delimiter_chars = set(delimiter_chars)
#
# Буквы из которых должно состоять слово.
letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
# letters = ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э']
letters = set(letters)
#
# Название текстового файла.
# file_name = 'Сказка о рыбаке и рыбке.txt'
# file_name = 'Толстой Война и мир.txt'
# file_name = 'Input_STR.txt'
file_name = 'Shakespeare William. Hamlet.txt'
#
# Откроем выбранный файл.
# Кодировки: encoding='utf-8' encoding='cp1251'
# with open(file_name, "r", encoding='utf-8') as text_io:
with open(file_name, "r", encoding='cp1251') as text_io:
    text = text_io.read()
#
print(f'Имя файла:\n'
      f'{file_name}\n'
      f'Всего: {len(text)} символов.\n')
#
# Очистим текст от лишних символов.
clear_text = set()
latch = False
word = ''
for char in text:
    if char in delimiter_chars:
        if latch:
            # Пропускаем все лишние символы
            continue
        else:
            latch = True
            # Добавим еще одно слово (в нижнем регистре) ко множеству слов.
            clear_text.add(f'{word.lower()}')
            word = ''
    else:
        latch = False
        word += char
#
# Из множества слов выберем только те, которые целиком состоят из указанных букв.
cherry_pick = []
for word in clear_text:
    if set(word).issubset(letters):
        cherry_pick.append(word)
#
# Напечатаем результат.
print(*sorted(cherry_pick))
