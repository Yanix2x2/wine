# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка
* Скачайте код
```bash
git clone https://github.com/Yanix2x2/wine.git
```
* Настройте виртуальное окружение:
    - Для Windows:
```bash
python -m venv env
venv\Scripts\activate
```
* Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

Cайт запускается командой:
```bash
python3 main.py
```
Для добавления своего файла необходимо указать путь до него, например:
```bash
python3 main.py wine.xlsx
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
