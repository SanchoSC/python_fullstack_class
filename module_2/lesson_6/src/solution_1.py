#Запрашиваем список и преобразуем его в массив
arr = str(input("Введите список продуктов через запятую:")).split(",")
#Считаем и выводим
print(arr[1:len(arr):2])