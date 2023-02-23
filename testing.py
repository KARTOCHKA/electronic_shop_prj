from clases import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print("-------------")

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)

print("-------------")

print(Item.all)
