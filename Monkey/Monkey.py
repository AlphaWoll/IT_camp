import sys
import select
import time
import os
import winsound
import msvcrt
from threading import Thread
import threading

clear = lambda: os.system('cls') #функция, которая очищает экран
snorepath = "C:\\Kharitonov\\snore.wav"
songpath = "C:\\Kharitonov\\mix.wav"

def morgat():
	q = "   /---\\ " # Все буквы - переменные
	x = "  /     \\"
	z = "  |  O  |"
	w = "  \\     /"
	a = "   \\___/ "
	y = "   -----"
	for i in range(2):
		print (q, q)
		print (x, x)
		print (z, z)
		print (w, w)
		print (a, a)
		time.sleep(2) #время остановки
		clear() #вызов функции 
		print ("\n\n",y, y)
		time.sleep(0.5) #время остановки
		clear() #вызов функции

class Monkey:
	issleep = True
	food = 100
	sleep = 100
	def __init__(self, name, sleep, food):
		self.name = name
		self.sleep = sleep
		self.food = food
	def Sleep(self):
		winsound.PlaySound(None, winsound.SND_PURGE)
		winsound.PlaySound(snorepath, winsound.SND_ASYNC)
		print("Hrr")
		self.sleep += 10 
		if self.sleep >= 100:
			self.sleep = 100
	def Wake(self):
		print("Накликайте 30 раз чтобы разбудить спящую обезбяну")
		start = time.time()
		kolvo = []
		PERIOD_OF_TIME = 5
		while True :
			if time.time() > start + PERIOD_OF_TIME : break
			ret = msvcrt.getch()
			kolvo.append(ret)

		print(len(kolvo))
		if len(kolvo)>30:
			print("Вы разбудили древнее зло")
		winsound.PlaySound(None, winsound.SND_PURGE)
		winsound.PlaySound(songpath, winsound.SND_ASYNC)
		morgat()
		self.issleep = False
	def Eat(self):
		print(self.name + " ест")
	def Sing(self):
		pass

e = Monkey("Ежан", 100, 100)

while True:  # Начинаем цикл
	stroka = input()  # Создаём переменную
	if stroka == ("Спи, " + e.name) and not e.issleep:
		e.Sleep()
	elif stroka == (e.name+" просыпайся") and e.issleep:
		e.Wake()
	else: # Если содержание переменной не совпадает с условием то...
		if e.issleep:
			e.Sleep()
		else:
			e.Wake()
	

while True:
	if e.issleep:
		while True:
			e.Sleep()
			if input()==(e.name+", просыпайся"): break
		e.Wake()
	else:
		while input()!=(r"Спи " + e.name):
			e.Sing()
		e.Sleep()
		e.issleep = True