import pytest
from string_utils import StringUtils

utils = StringUtils()

# Проверки capitilize


@pytest.mark.parametrize("stringValue, result", [("skypro", "Skypro"), ("helen", "Helen"), ("mayakovsky", "Mayakovsky"),
("12345", "12345"), ("", ""), (" ", " ")])
def test_capitilize(stringValue, result):
    assert utils.capitilize(stringValue) == result


# Проверки trim
@pytest.mark.parametrize("stringValue, result", [(" Hello", "Hello"), ("  Helen", "Helen"), ("  Hello Mir", "Hello Mir"),
("1234", "1234"), ("", ""), (" ", "")])
def test_trim(stringValue, result):
    assert utils.trim(stringValue) == result


# Проверки to_list
@pytest.mark.parametrize("input, delimetr, result", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("father,mother,daughter,son", ",", [
        "father", "mother", "daughter", "son"]),
    ("5:4:3:2", ":", ["5", "4", "3", "2"]),
    ("", ",", []),
    (" ", ",", []),
    ("None",",",["None"])
])
def test_to_list(input, delimetr, result):
    assert utils.to_list(input, delimetr) == result


# Проверки Contains
@pytest.mark.parametrize("input, value, result", [("Container", "n", True), ("Container", "z", False),
("None", "None", True), ("1234", "2", True), ("", "", True), (" ", "", True)])
def test_contains_(input, value, result):
    assert utils.contains(input, value) == result


# Проверки для Delete
@pytest.mark.parametrize("input, value, result", [("Container", "Con", "tainer"), ("Container", "ta", "Coniner"),
("Container123", "er123", "Contain"), ("1234", "12", "34"), 
("None", "e", "Non"), ("", "", ""), (" ", "", " ")])
def test_delete(input, value, result):
    assert utils.delete_symbol(input, value) == result


# Проверки starts_with
@pytest.mark.parametrize("input, value, result", [("Container", "C", True), ("Container", "T", False), ("123", "123", True),
(" None", "N", False), ("", "", True), (" ", " ", True)])
def test_starts(input, value, result):
    assert utils.starts_with(input, value) == result


# Проверки end_with
@pytest.mark.parametrize("input, value, result", [("Container", "r", True), ("Container", "n", False), ("12345", "45", True),
("123abc  ", "  ", True), ("  ", "", True), ("", "", True), ("None", "", True)])
def test_end_with(input, value, result):
    assert utils.end_with(input, value) == result


# Проверки is_empty
@pytest.mark.parametrize("input, result", [("", True), (" ", True), ("    ", True), ("Barometr", False), ("123", False)])
def test_is_empty(input, result):
    assert utils.is_empty(input) == result


# Проверки list_to_string
@pytest.mark.parametrize("list, joiner, result", [
    (["father", "mother", "daughter", "son"], ",", "father,mother,daughter,son"),
    ([5, 4, 3, 2], ",", "5,4,3,2"),
    (["Rostov", "Na", "Dony"], "-", "Rostov-Na-Dony"), ([], ",", ""), ([0], ",", "0"),
    (["None"], ",", "None")
])
def test_list_to_string(list, joiner, result):
    assert utils.list_to_string(list, joiner) == result
