#Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах:'))
hour = time // 3600
minutes = (time - hour) // 60
seconds = time - ((hour * 3600) + (minutes*60))
print ( f'Время в формате чч:мм:сс  { hour }:{ minutes }:{ seconds }' )

