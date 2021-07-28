# создайте константу MINUTES_IN_HOUR
# < напишите код здесь >
MINUTES_IN_HOURS = 60
def minutes_to_hours(minutes):
    return minutes/MINUTES_IN_HOURS

print('Длина фильма "Форма воды": {:.2f} ч.'.format(minutes_to_hours(123)))