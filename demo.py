stock = [
    ["JBL", "XYZ 123", 1500, 40],
    ["Sony", "gggg 89", 2000, 13],
    ["Beats", "chachacha", 3500, 0]
]

stock = [
    {
        "brand": "JBL",
        "model": "XYZ 123",
        "price": 1500,
        "qty": 40
    },
    {
        "price": 2000,
        "brand": "Sony",
        "model": "gggg 89",
        "qty": 13
    },
    {
        "price": 3500,
        "model": "chachacha",
        "brand": "Beats",
        "qty": 0
    }
]



# for item in stock:
#     print(f"Brand: {item['brand']}, Model: {item['model']}, Price: {item['price']}, Stock Qty: {item['qty']}")

list_item = [
    "Beats",
    "chachacha",
    3500,
    0
]

list_item.append("red")

# print(list_item)


item = {
    "price": 3500,
    "model": "chachacha",
    "brand": "Beats",
    "qty": 0
}

key = "price"

# print(item[key])

# dve varianty jak vytvorit prazdny slovik
empty_dict = {}
empty_dict = dict()




# -------------------------- Slovniky a cykly
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Klice = keys
for houba in sales.keys():
    print(houba)

# =

# for key in sales:
#     print(key)

# Hodnoty = values
for hrib in sales.values():
    print(hrib)

#   = items
for lysohlavka, muchomurka in sales.items():
    print(f"Klic: {lysohlavka}, Hodnota: {muchomurka}")
