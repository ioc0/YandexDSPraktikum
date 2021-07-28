# Записываем курс в переменной rubles_for_dollar
# (англ. rubles for dollar, "рублей за доллар").
rubles_for_dollar = 67.01

def print_budget_in_rubles(money):

    print('Бюджет: {:.2f} млн ₽'.format(money*rubles_for_dollar))

print('Титаник')
print_budget_in_rubles(200.0)
print()
print('Гладиатор')
print_budget_in_rubles(103.0)