from datetime import datetime, timedelta
try:
    print('Введите дату отправления поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
    start_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except:
    print('Дата в неверном формате')
    exit()

try:
    print('Введите время в пути (часы/минуты):')
    hours = int(input('часы = '))
    minutes = int(input('минуты = '))
except:
    print('Вы ввели не целое число')
    exit()
    
if hours < 0 or minutes < 0:
    print('Время в пути не может быть отрицательным')
    exit()
# Преобразуем время в пути к типу timedelta, который позволяет совершать действия с временем
travel_time = timedelta(hours=hours, minutes=minutes)
# Прибавляем к времени старта время в пути. Такое действие доступно именно для типа timedelta
pribitie_date = start_date + travel_time
print('Время прибытия', pribitie_date)