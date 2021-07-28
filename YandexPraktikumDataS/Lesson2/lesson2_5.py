
"""Оценим, какую долю в EmojiXpress составляют выбранные нами эмодзи. Всего в сообщениях с клавиатуры
EmojiXpress их отправлено 1.72 миллиарда, или 1720 миллионов. Сложите количества всех эмодзи из таблицы и сумму
поделите на 1720. Результат выведите в процентах с точностью до одного знака после запятой (уже сделано в прекоде).
"""
'''
emojixpress = [
    2.26,
    19.1,
    25.6,
    233.0,
    15.2,
    22.7,
    64.6,
    87.5,
    6.81,
    6.0,
    4.72,
    24.7,
    21.7,
    10.0,
    118.0,
    3.31,
    23.1,
    1.74,
    4.5,
    0.0333,
]
emojixpress_total = 1720


selected_total = 0
for count in emojixpress:
    selected_total += count

selected_part = selected_total/emojixpress_total
print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(selected_part))
'''
twitter = [
    87.3,
    150,
    0.0,
    2270.0,
    264.0,
    565.0,
    834.0,
    432.0,
    0.0,
    478.0,
    198.0,
    654.0,
    98.7,
    445.0,
    1080.0,
    697.0,
    227.0,
    0.0,
    150.0,
    932.0,
]
twitter_total = 24500

selected_emoji = 0
for item in twitter:
    selected_emoji+=item
selected_part = selected_emoji/twitter_total
print('Доля выбранных эмодзи в Твиттере: {:.1%}'.format(selected_part))