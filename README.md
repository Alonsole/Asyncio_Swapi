## Домашнее задание к лекции "Event loop. Asyncio"

Цель выгружать из API персонажей Start Wars и загружать в базу данных.  
Документация по API находится здесь: [SWAPI](https://swapi.py4e.com/documentation).  
Пример запроса: https://swapi.py4e.com/api/people/1/  
В результате запроса получаем персонажа с ID 1:  
```
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "hair_color": "blond",
  "skin_color": "fair",
  "eye_color": "blue",
  "birth_year": "19BBY",
  "gender": "male",
  "homeworld": "https://swapi.py4e.com/api/planets/1/",
  "films": [
    "https://swapi.py4e.com/api/films/1/",
    "https://swapi.py4e.com/api/films/2/",
    "https://swapi.py4e.com/api/films/3/",
    "https://swapi.py4e.com/api/films/6/",
    "https://swapi.py4e.com/api/films/7/"
  ],
  "species": [
    "https://swapi.py4e.com/api/species/1/"
  ],
  "vehicles": [
    "https://swapi.py4e.com/api/vehicles/14/",
    "https://swapi.py4e.com/api/vehicles/30/"
  ],
  "starships": [
    "https://swapi.py4e.com/api/starships/12/",
    "https://swapi.py4e.com/api/starships/22/"
  ],
  "created": "2014-12-09T13:50:51.644000Z",
  "edited": "2014-12-20T21:17:56.891000Z",
  "url": "https://swapi.py4e.com/api/people/1/"
}
```
## Функциональные возможности

- Асинхронные запросы на целевой API
- Обработка полученных json в нужный формат для загрузки в PostgreSQL
- Загрузка а базу данных
- БД запускается контейнером Docker

## Стек технологий

- База данных: PostgreSQL
- Работа с API: aiohttp + asyncio
- Для подсчёта времени выполнения: datetime

## Установка и запуск проекта, полезная информация
[Документация](https://github.com/Alonsole/Asyncio_Swapi/blob/main/Documentation.md)

### Требования

- Python 3.10 +
- PostgreSQL
- Docker Desktop (опционально)


### Клонируйте репозиторий:

```
git clone git@github.com:Alonsole/Asyncio_Swapi.git
```

### Установите виртуальную среду и активируйте ее:
Понадобится для тестов вне Контейнеров
```
python3 -m venv venv
source venv/bin/activate
```

## Лицензия
Это учебный проект вне коммерческих целей.
## Контакты
Проект не предполагает взаимодействий с пользователями.
