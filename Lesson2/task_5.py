def month_to_season(month):
    month_m=["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
    result=month_m[month-1]
    return result

month = input("Введите месяц: ")
month= int(month)
print(month_to_season(month))