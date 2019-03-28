# IT_camp
Only for AItyata
import os  #импорт в ОС
import time #импорт Времени
clear = lambda: os.system('cls') #функция, которая очищает экран
def morgat():
	q = "   /---\\ " # Все буквы - переменные
	x = "  /     \\"
	z = "  |  O  |"
	w = "  \\     /"
	a = "   \\___/ "
	y = "   -----"
	f = "_______"
	g = "\\_____/"
	while True: #пока правда:
		print ( q,  q)
		print (x, x)
		print (z, z)
		print (w, w)
		print (a,  a)
		print ("\n\n       ",g)
		time.sleep(2) #время остановки
		clear() #вызов функции 
		print ("\n\n",y, y)
		print ("\n\n       ",f)
		time.sleep(0.5) #время остановки
		clear() #вызов функции
morgat()
