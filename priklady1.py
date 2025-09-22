# Task 01
school_report = {
    "cesky jazyk": 2,
    "matematika": 1,
    "dejepis": 4
}

# print(school_report)

# Task 02
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100

# print(sales)

# Task 03
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

number = int(input("Zadej sve cislo: "))

if number in tombola:
    print(f"Vyhral*a jsi! Tvou cenou je: {tombola[number]}")
else:
    print("Bohuzel nevyhravas nic.")
