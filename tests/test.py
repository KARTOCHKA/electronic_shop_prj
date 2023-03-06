import pytest
from main.clases import Item, Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_electronic_store_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.ammount == 20
    assert item.pay_rate == 1


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_discount_price(item):
    assert item.apply_discount() == 10000


def test_is_integer(item):
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_repr(item):
    assert item.__repr__() == 'Item(Смартфон, 10000, 20)'


def test_str(item):
    assert item.__str__() == 'Смартфон'


def test_add(item):
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone + item == 25


def test_phone_init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.ammount == 5
    assert phone.number_of_sim == 2


def test_phone_number_of_sim(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_phone_repr(phone):
    assert repr(phone) == 'Phone(iPhone 14, 120000, 5, 2)'



