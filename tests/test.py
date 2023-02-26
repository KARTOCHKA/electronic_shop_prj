from main.clases import Item


def test_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8  # устанавливаем новый уровень цен
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000
    item2.apply_discount()
    assert item2.price == 16000.0
    assert len(Item.all) == 2

