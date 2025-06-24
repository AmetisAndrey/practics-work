import pytest
from main import validate_type

@pytest.mark.parametrize("value,expected", [
    ("vasya@pku.ln.ru", "email"),
    ("+7 123 456 78 90", "phone"),
    ("27.05.2025", "date"),
    ("2025-05-27", "date"),
    ("hello", "text"),
    ("12345", "text"),
])
def test_detect_type(value, expected):
    assert validate_type(value) == expected
