def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def get_first_word(sentence):
    return sentence.split()[0]


# Тесты для add()
def test_add_positive():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 10) == 10

def test_add_negative():
    assert add(-1, -1) == -2


# Тесты для is_even()
def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(3) == False

def test_is_even_zero():
    assert is_even(0) == True


# Тесты для get_first_word()
def test_first_word():
    assert get_first_word("hello world") == "hello"

def test_first_word_single():
    assert get_first_word("python") == "python"