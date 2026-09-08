import pytest

def test_first():
    assert 2+2==4
    assert 10-3==7
    assert 10*3==30

def test_string():
    name= "Sveta"
    assert name == "Sveta"
    assert len(name) == 5
    assert name.upper() == "SVETA"

def test_list():
    num= [1,2,3]
    assert 2 in num
    assert len(num) == 3
    assert num[0] == 1

def add(a,b):
    return a+b

def is_even(num):
    return num % 2 == 0

def get_discount_price(price, discount_price):
    return  price-price * discount_price/100

def test_add():
    assert add(1,2) == 3
    assert add(-1,2)== 1
    assert add(0,0) == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_discount():
    assert get_discount_price(100, 20)==80
    assert get_discount_price(100, 0)==100

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (4,5,9),
    (-1,-1,-2),
    (0,0,0),
])
def test_add_partial(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.parametrize("num,expected", [   #yksi testi moto asia
    (1,False),
    (2,True),            #ensimainen mitä toinen tulos
    (3,False),
    (4,True),
])
def test_is_even_parametrize(num,expected):
    assert is_even(num) == expected

@pytest.fixture
def my_user():
    return {"name":"Sveta","age":18,"email":"egtrth525@dkd.ddf"}

def test_user_name(my_user):
    assert my_user["name"] == "Sveta"

def test_user_age(my_user):
    assert my_user["age"]==18
    assert my_user["age"] > 17
