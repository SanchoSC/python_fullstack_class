#Запрашиваем список и преобразуем его в массив чисел
arr = list(map(int,input("Введите список цен через запятую:").split(",")))
positions = list(map(int,input("Введите позиции для перестановки через запятую:").split(",")))
#Заранее записываем значения и их индексы, чтобы во время смены цен не было ошибки
x = arr[positions[0]]
arr[positions[0]] = arr[positions[1]]
arr[positions[1]] = x
#Выводим результат
print(arr)