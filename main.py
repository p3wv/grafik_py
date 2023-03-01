import datetime
import calendar
import pandas as pd
import random



class Kierowca:
    def __init__(self, godziny_dostepne, dni_wolne) -> None:
        self.godziny_dostepne = godziny_dostepne
        self.dni_wolne = dni_wolne



curr_year = datetime.datetime.now().year
curr_month = datetime.datetime.now().month




x = input('podaj ilosc max h/msc: ')

y = input('dni wolne yyyy-mm-dd: ').split('-') # user chooses the days of the month


year, month, day = [int(item) for item in y]

d = datetime.date(year, month, day)

tdd = d.strftime('%Y-%m-%d')






td = datetime.date.today().replace(day=1) #get first day of the month
last_day = datetime.date.today().replace(day=calendar.monthrange(curr_year, curr_month)[1]) #get last day of the month

# last_day = datetime.datetime.today().replace(day=)

# td1 = datetime.datetime.today().replace(day=last_day)

zasieg = pd.date_range(td, last_day)






if __name__ == "__main__":

    print("godz max kierowcy: ", x, y)
    print("wybrane dni wolne: ", d)
    print("datetime w stringu: ", tdd)

    print("current month: ", datetime.datetime.now().month)
    print(calendar.monthrange(curr_year, curr_month))
    print("pierszy msc, last miesiaca: ", td, last_day)
    print("zasieg: ", zasieg)

    grafik=zasieg[zasieg != tdd]
    print("grafik (zasieg - dni wolne): ", grafik)

    monthly_hours = 0

    dni_do_obsadzenia = []

    for i in grafik:

        dni_powszednie_etc = datetime.date.weekday(i)

        if dni_powszednie_etc in range(0,4):
            monthly_hours += 12
            dni_do_obsadzenia.append(dni_powszednie_etc)
        elif dni_powszednie_etc == 5:
            monthly_hours += 13.5
            dni_do_obsadzenia.append(dni_powszednie_etc)
        else:
            monthly_hours += 11
            dni_do_obsadzenia.append(dni_powszednie_etc)

    print("monthly hours available: ", monthly_hours)

    print(dni_do_obsadzenia)


    weekend_5 = ["11-21", "13-23", "17-24"]
    weekend_6_or_weekday = ["11-21", "13-23", "17-23"]

    grafik_final = []

    for i in dni_do_obsadzenia:
        if i in range(0, 4):
            grafik_final.append(random.choice(weekend_6_or_weekday))
        elif i == 5:
            grafik_final.append(random.choice(weekend_5))
        elif i == 6:
            grafik_final.append(random.choice(weekend_6_or_weekday))

    print(grafik_final)

    godziny_kier = 0

    for i in grafik_final:
        i.split("-")
        h1, h2 = [int(z) for z in i]
        godziny_kier += h2 - h1

    print(godziny_kier)

    # assigning random working hours: