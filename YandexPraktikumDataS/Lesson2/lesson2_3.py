"""
Найдите сумму первых пяти элементов подготовленного списка emojixpress. Но складывайте не сами числа,
а элементы, полученные по индексу. Напечатайте результат на экране (формат вывода уже задан в прекоде).

"""
emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

total = sum(emojixpress[i] for i in range(5))
print('{:.2f}'.format(total))
total2 = emojixpress[0] + emojixpress[1] + emojixpress[2] + emojixpress[3]+ emojixpress[4]
print('{:.2f}'.format(total2))