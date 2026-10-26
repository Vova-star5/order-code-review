# ============================================
# МОДУЛЬ: ОФОРМЛЕНИЕ ЗАКАЗА
# ПРОЕКТ: ИНТЕРНЕТ-МАГАЗИН
# АВТОР: КОЛЛЕГА
# ============================================

# Список товаров в корзине (цена в рублях)
tovary = [1500, 2500, 750, 3200]

# Функция для подсчёта общей стоимости заказа
def summa_zakaza(spisok):
    summa = 0
    for i in range(len(spisok)):
        summa = summa + spisok[i]
    return summa

# Функция для применения скидки
def skidka(summa, procent):
    if procent > 0:
        itog = summa - (summa * procent / 100)
    else:
        itog = summa
    return itog

# Функция для расчёта доставки
def dostavka(summa, gorod):
    if gorod == "Москва":
        if summa > 5000:
            return 0
        else:
            return 300
    elif gorod == "Санкт-Петербург":
        if summa > 7000:
            return 0
        else:
            return 400
    else:
        return 500

# Основная программа
print("Оформление заказа")
print("==================")

# Выводим товары
print("Товары в корзине:")
for i in range(len(tovary)):
    print(str(i + 1) + ". " + str(tovary[i]) + " руб.")

# Считаем сумму
obshaya_summa = summa_zakaza(tovary)
print("")
print("Общая сумма: " + str(obshaya_summa) + " руб.")

# Запрашиваем данные покупателя
imya = input("Введите ваше имя: ")
adres = input("Введите адрес доставки: ")
telefon = input("Введите номер телефона: ")

# Проверяем телефон
if len(telefon) != 11:
    print("Ошибка: номер телефона должен содержать 11 цифр")
else:
    print("Телефон принят")

# Запрашиваем скидку
promokod = input("Введите промокод (если есть): ")
if promokod == "SKIDKA10":
    procent_skidki = 10
elif promokod == "SKIDKA20":
    procent_skidki = 20
else:
    procent_skidki = 0

# Применяем скидку
summa_so_skidkoy = skidka(obshaya_summa, procent_skidki)
print("Сумма со скидкой: " + str(summa_so_skidkoy) + " руб.")

# Запрашиваем город доставки
gorod = input("Введите город доставки: ")

# Считаем доставку
stoimost_dostavki = dostavka(summa_so_skidkoy, gorod)
print("Стоимость доставки: " + str(stoimost_dostavki) + " руб.")

# Считаем итоговую сумму
itogovaya_summa = summa_so_skidkoy + stoimost_dostavki
print("ИТОГО К ОПЛАТЕ: " + str(itogovaya_summa) + " руб.")

# Сохраняем заказ в файл
f = open("zakaz.txt", "w")
f.write("Имя: " + imya + "\n")
f.write("Адрес: " + adres + "\n")
f.write("Телефон: " + telefon + "\n")
f.write("Город: " + gorod + "\n")
f.write("Сумма: " + str(itogovaya_summa) + "\n")
f.close()
print("Заказ сохранён в файл zakaz.txt")
