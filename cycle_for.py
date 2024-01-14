car_list = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA', 'TOYOTA']
for stamp in car_list:
    print('Я езжу на автомобиле марки', stamp)
    if stamp == 'TOYOTA':
         print('Это верно! :)')
         break
    print('Это не верно...')
cars_count = 0
for stamp in car_list:
    cars_count += 10
    pass
print('Всего автомобилей', cars_count, 'шт')
