def SpiMonkey():   # Создаём метод

	import winsound  # Связываем с winsound'ом 

	while True:  # Начинаем цикл
		stroka = input()  # Создаём переменную
		if stroka == "Спи, Обезьяна":  # Создаём условие (Конструкцию 'if')
			break  # Если содержание переменной совпадает с условием то цикл заканчивается

		else: # Если содержание переменной не совпадает с условием то...
			print("Обезьяна продолжает петь!") # Выводим текст

	winsound.PlaySound("C:\\Kashin\\02654wavwav.wav", 0)  # Запускаем звук храпа прописывая путь

SpiMonkey()  # Вызываем метод