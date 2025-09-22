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
# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# # Klice = keys
# for houba in sales.keys():
#     print(houba)

# # =

# # for key in sales:
# #     print(key)

# # Hodnoty = values
# for hrib in sales.values():
#     print(hrib)

# #   = items
# for lysohlavka, muchomurka in sales.items():
#     print(f"Klic: {lysohlavka}, Hodnota: {muchomurka}")

# print(sum(sales.values()))

books = [ # seznam (list)
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

book = books[0] # slovnik (dict)
        # { "title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018 }

sold_qty = book["sold"] # cislo (int)


total_sales = 0
for slovnik in books:
    total_sales += slovnik["sold"]

print(f"Celkem bylo prodáno {total_sales} knih.")


names = set()

names.add('Martin')
names.add('Jana')
names.add('Petr')
names.add('Simona')
print(len(names), names)

names.add('Martin')
print(len(names), names)
