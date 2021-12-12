# Tests API for WOT
Проект автотестов API

#### Стэк
- язык программирования - [Python 3.9](https://www.python.org/downloads/)
- тестовый фреймворк - [pytest](https://docs.pytest.org/en/latest/)
- api-автоматизация - [requests](https://requests.readthedocs.io/en/master/)
- отчеты - [allure](https://docs.qameta.io/allure/)
- (де)сериализация - [pydantic](https://pydocs.helpmanual.io/)
- матчеры - [assertpy](https://github.com/assertpy/assertpy)

#### Структура
```bash
.
├── data			# модели данных
├── tests			# тесты
│   ├── account			# раздел Аккаунт
│   └── authentication		# раздел Аутентифакация 
├── .gitignore			# список игнорируемых гитом файлов, папок    
├── Dockerfile			# команды создания образа docker
└── requirements.txt		# подключение внешних библиотек
```

## Установка
1. Клонируем проект
<br>`git clone https://github.com/vumnyi/wot_api_testing.git`
2. В проекте устанавливаем виртуальное окружение [virtualenv](https://virtualenv.pypa.io/en/latest/) и активируем его:
<br> Windows `venv\Scripts\activate.bat`
<br> MacOS/Linux `source venv/bin/activate`
<br> PyCharm - следуем подсказкам или через настройки добавляем интерпретатор
3. Устанавливаем все зависимости из файла `requirements.txt`
<br> `pip install -r requirements.txt`
4. Скачать пакет [allure](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.9.0/allure-commandline-2.9.0.zip). Архив распаковать в каталоге проекта в отдельной папке: ./allure-cli

## Запуск в Docker
- создание образа **Docker**, выполнить в терминале из папки с проектом:
<br>`docker build -t api_tests .`
- для запуска тестов в Docker:
<br>`docker run -v C:\\Python_projects\\wot_api_testing:/app api_tests pytest -v -l --alluredir=allure-results \tests`

## Запуск локально
<br>`pytest -v -l --alluredir=allure-results .\tests`, выполнить в терминале из папки с проектом
## Сформировать отчет:
<br>`\allure-cli\bin\allure serve .\allure-results`

