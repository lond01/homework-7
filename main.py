
from datetime import date

year = int(input("Введіть рік: "))
month = int(input("Введіть місяць: "))
day = int(input("Введіть день: "))

target_date = date(year, month, day)
today = date.today()

days_left = (target_date - today).days

if days_left > 0:
    print(f"До заданої дати залишилося {days_left} днів.")
elif days_left == 0:
    print("Ця дата сьогодні!")
else:
    print(f"Ця дата минула {abs(days_left)} днів тому.")
