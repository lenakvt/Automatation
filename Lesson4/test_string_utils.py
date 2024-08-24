import pytest
from string_utils import StringUtils

utils = StringUtils()

# Проверки capitilize


@pytest.mark.parametrize("stringValue, result", [("skypro", "Skypro"), ("скайпро", "Скайпро"), ("555", "555")])
def test_capitilize_positive(stringValue, result):
    assert utils.capitilize(stringValue) == result


@pytest.mark.xfail
@pytest.mark.parametrize("stringValue, result", [("i love Spb", "I love Spb"), ("skypro", "Skypr"), ("555Rus", "555Rus")])
def test_capitilize_negative(stringValue, result):
    assert utils.capitilize(stringValue) == result


# Проверки trim
@pytest.mark.parametrize("stringValue, result", [(" Hello", "Hello"), ("He llo", "He llo"), (" Hello Mir", "Hello Mir")])
def test_trim_positive(stringValue, result):
    assert utils.trim(stringValue) == result


@pytest.mark.xfail
@pytest.mark.parametrize("stringValue, result", [(" 555", " 555"), (" Hello ", "Hello"), ("Hello Mir", " HelloMir")])
def test_trim_negative(stringValue, result):
    assert utils.trim(stringValue) == result


# Проверки to_list
@pytest.mark.parametrize("input, delimetr, result", [
    ("father,mother,daughter,son", ",", [
     "father", "mother", "daughter", "son"]),
    ("5:4:3:2", ":", ["5", "4", "3", "2"]),
    ("", ",", []),
])
def test_to_list_positive(input, delimetr, result):
    assert utils.to_list(input, delimetr) == result


@pytest.mark.xfail
@pytest.mark.parametrize("input, delimeter, result", [
    ("father, mother, daughter, son", ",", [""]),
    ("fat her", " ", ["father"]),
    ("", ",", [" "]),
])
def test_to_list_negative(input, delimeter, result):
    assert utils.to_list(input, delimeter) == result


# Проверки Contains
@pytest.mark.parametrize("input, value, result", [
    ("Container", "n", True),
    ("Container", "z", False),
    ("Container", "Container", True)
])
def test_contains_positive(input, value, result):
    assert utils.contains(input, value) == result


@pytest.mark.xfail
@pytest.mark.parametrize("input, value, result", [
    ("Container","N", True),
    ("Container","", False),
    (" "," ", False)
])
def test_contains_negative(input, value, result):
    assert utils.contains(input, value) == result
    

#Проверки для Delete
@pytest.mark.parametrize("input, value, result",[
    ("Container", "Con","tainer"),
    ("Container","ta","Coniner"),
    ("Container123","er", "Contain123")
])
def test_delete_positive(input, value, result):
    assert utils.delete_symbol(input, value) == result
    
    
@pytest.mark.xfail
@pytest.mark.parametrize("input, value, result", [
    ("Container", "Con","Tainer"),
    ("Container","Ta","Coniner"),
    ("None","4", "Non")
])
def test_delete_negative(input, value, result):
    assert utils.delete_symbol(input, value) == result   