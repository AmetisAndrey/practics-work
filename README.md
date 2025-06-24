## Описание

Программа позволяет найти подходящий шаблон формы на основе переданных параметров. Используется база данных TinyDB.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python app.py get_tpl --имя_поля=значение
```

Примеры:

```bash
python app.py get_tpl --login=vasya@example.com --tel=+7 912 345 67 89
```

## Тесты

```bash
pytest tests/
```

## Структура проекта

- `app.py` — основная логика;
- `data/db.json` — шаблоны форм;
- `tests/test_app.py` — тесты;
- `requirements.txt` — зависимости;
- `README.md` — инструкция.