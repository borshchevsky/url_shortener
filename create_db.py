from shortener import create_app, db

# Создаём таблицы модели в базе
db.create_all(app=create_app())
