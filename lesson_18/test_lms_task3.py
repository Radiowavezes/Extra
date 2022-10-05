from lms_task3 import TypeDecorators


def test_to_int():
    @TypeDecorators.to_int
    def func(strng):
        return strng

    assert func('25') == 25
    assert func(1.5) == 1
    assert func('ty') != 'ty'

def test_to_float():
    @TypeDecorators.to_float
    def func(strng):
        return strng

    assert isinstance(func(11), float)
    assert isinstance(func(0), float)

def test_to_str():
    @TypeDecorators.to_str
    def func(strng):
        return strng
    
    assert isinstance(func(11), str)
    assert isinstance(func([1, 2, 3]), str)
    assert isinstance(func({1:1, 2:2}), str)
