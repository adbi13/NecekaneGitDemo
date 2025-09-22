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

print(item[key])

# dve varianty jak vytvorit prazdny slovik
empty_dict = {}
empty_dict = dict()

