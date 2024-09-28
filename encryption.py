d = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ь': 28, 'ы': 29, 'ъ': 30, 'э': 31, 'ю': 32, 'я': 33, '-': 34, '.': 35, ',': 36, '...': 37, '!': 38, '?': 39, ':': 40, ' ': 41}

d2 = {1: 'а', 2: 'б', 3: 'в', 4: 'г', 5: 'д', 6: 'е', 7: 'ё', 8: 'ж', 9: 'з', 10: 'и', 11: 'й', 12: 'к', 13: 'л', 14: 'м', 15: 'н', 16: 'о', 17: 'п', 18: 'р', 19: 'с', 20: 'т', 21: 'у', 22: 'ф', 23: 'х', 24: 'ц', 25: 'ч', 26: 'ш', 27: 'щ', 28: 'ь', 29: 'ы', 30: 'ъ', 31: 'э', 32: 'ю', 33: 'я', 34: '-', 35: '.', 36: ',', 37: '...', 38: '!', 39: '?', 40: ':', 41: ' '}


def encrypt(text: str, key: int, alp_len: int) -> str:
    '''Функция шифрования по алгоритму Цезаря. АЛФАВИТ ДОЛЖЕН НАЧИНАТЬСЯ С 1!!!'''
    
    new_text = ''
    for char in text:
        new_char = (d[char] + key + 1) % (alp_len + 1) if d[char] + key > alp_len else d[char] + key

        new_text += str(new_char) + '-'
    return new_text[:-1]

def decrypt(text: str, key: int, alp_len: int) -> str:
    '''Функция расшифрования по алгоритму Цезаря. АЛФАВИТ ДОЛЖЕН НАЧИНАТЬСЯ С 1!!!'''
    
    max_value_in_alp = alp_len - (key % (alp_len + 1) if key > alp_len else key) 

    old_text = ''
    for char in text.split('-'):
        new_char = d2[int(char) + max_value_in_alp - (alp_len + 1) if int(char) + max_value_in_alp > alp_len else int(char) + max_value_in_alp] \
            if int(char) - key <= 0 else d2[int(char) - key]
        old_text += new_char
    return old_text
