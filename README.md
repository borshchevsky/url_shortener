# URL Shortener API

Создаёт короткие ссылки.<br>
Пример:

http://www.example.com -> http://host/alJND


### Пример использования API на Python:


```sh
$ import requests
$ 
$ json = {'url': 'http://exampleurl.com'}
$ r = r.post('http://api.host', json=json)
```
```sh
response:

{
'short_url': 'http://host/alJND'
}
```
http://host/alJND перенаправляет по исходной ссылке http://exampleurl.com<br>
<br>
Посмотреть статистику посещений конкретной короткой ссылки: <br>
<br>
http://api.host/statistics/alJND
<br><br>
### Установка
1. Установить зависимости

```sh
$ pip install -r requirements.txt
```

2. Создать таблицы в базе

```sh
$ python create_db()
```