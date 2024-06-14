# Словарь для замены русских букв на английские в соответствии с раскладкой клавиатуры
translit_dict = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k',
    'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm',
    'б': ',', 'ю': '.', 'ё': '`'
}

def translate_to_english(word):
    # Переводим каждую букву слова в соответствии с раскладкой
    translated_word = ''.join([translit_dict.get(char, char) for char in word])
    return translated_word

# Пример использования
word = input("Введите слово: ")
translated_word = translate_to_english(word)
print("Переведенное слово:", translated_word)
