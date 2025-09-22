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
        "brand": "Sony",
        "model": "gggg 89",
        "price": 2000,
        "qty": 13
    },
    {
        "brand": "Beats",
        "model": "chachacha",
        "price": 3500,
        "qty": 0
    }
]



for item in stock:
    print(f"Brand: {item['brand']}\tModel: {item['model']}\tPrice: {item['price']}\tStock Qty: {item['qty']}")

