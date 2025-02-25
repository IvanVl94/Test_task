
from String_Utils import StringUtils

class TestStringUtils:
    # Позитивные тесты
    

    def test_to_uppercase(self):
        assert StringUtils.to_uppercase("test") == "TEST"
        assert StringUtils.to_uppercase("123") == "123"
        assert StringUtils.to_uppercase("04 апреля 2023") == "04 АПРЕЛЯ 2023"

    def test_to_lowercase(self):
        assert StringUtils.to_lowercase("TEST") == "test"
        assert StringUtils.to_lowercase("123") == "123"
        assert StringUtils.to_lowercase("04 апреля 2023") == "04 апреля 2023"

    def test_capitalize(self):
        assert StringUtils.capitalize("test") == "Test"
        assert StringUtils.capitalize("tESt") == "Test"
        assert StringUtils.capitalize("  test") == "  test"

    def test_reverse(self):
        assert StringUtils.reverse("test") == "tset"
        assert StringUtils.reverse("123") == "321"
        assert StringUtils.reverse("04 апреля 2023") == "3202 ялрепа 40"
    
    # Негативные тесты
    
    def test_to_uppercase_empty(self):
        assert StringUtils.to_uppercase("") == ""

    def test_to_lowercase_empty(self):
        assert StringUtils.to_lowercase("") == ""

    def test_capitalize_empty(self):
        assert StringUtils.capitalize("") == ""

    def test_reverse_empty(self):
        assert StringUtils.reverse("") == ""

    def test_to_uppercase_spaces(self):
        assert StringUtils.to_uppercase(" ") == " "

    def test_to_lowercase_spaces(self):
        assert StringUtils.to_lowercase(" ") == " "

    def test_capitalize_spaces(self):
        assert StringUtils.capitalize(" ") == " "

    def test_reverse_spaces(self): 
        assert StringUtils.reverse(" ") == " "

    def test_to_uppercase_none(self):
        assert StringUtils.to_uppercase(None) is None

    def test_to_lowercase_none(self):
        assert StringUtils.to_lowercase(None) is None

    def test_capitalize_none(self):
        assert StringUtils.capitalize(None) is None

    def test_reverse_none(self):
        assert StringUtils.reverse(None) is None