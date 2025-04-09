import random

zbozi = ["chleba", "kolo", "sýr", "auto", "triko", "mikia", "počítač", "schnitzel", "hranolky", "pizza"]


for i in range(11):
    osoba1 = random.choice(zbozi)
    print(f"Kupme {osoba1}")
    osoba2 = random.choice(zbozi)
    print(f"Ne, kupme {osoba2}")