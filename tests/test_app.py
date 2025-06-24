import subprocess
import os

def run_app(args):
    result = subprocess.run(["python3", "main.py", "get_tpl"] + args,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            cwd=os.path.dirname(__file__) + "/..")
    return result.stdout.strip()

def test_match_user_data():
    output = run_app(["--login=vasya@example.com", "--tel=+7 912 345 67 89"])
    assert output == "Данные пользователя"

def test_match_order_form():
    output = run_app(["--customer=Ivan", "--order_id=123", "--дата_заказа=27.05.2025", "--contact=+7 921 000 00 00"])
    assert output == "Форма заказа"

def test_match_partial():
    output = run_app(["--f_name1=aag@bbb.ru", "--f_name2=27.05.2025"])
    assert output == "Проба"

def test_no_match_output_type_detection():
    output = run_app(["--login=vasya", "--f_name2=27.05.2025"])
    assert '"login": "text"' in output
    assert '"f_name2": "date"' in output

def test_no_match_full():
    output = run_app(["--tumba=27.05.2025", "--yumba=+7 903 123 45 78"])
    assert '"tumba": "date"' in output
    assert '"yumba": "phone"' in output