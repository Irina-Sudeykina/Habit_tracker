# Проект "Habit_tracker" - Трекер привычек

## Описание:
 Проект "Habit_tracker" - это проект на Python, 
 передставляющи собой трекер привычек
 
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/Habit_tracker.git
 
 ```

 2. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:

### Модель User: ###
Модель представляет пользователя платформы, и имеет следующие свойства:<br>
email - Email,<br>
phone - Телефон,<br>
tg_nick - Ник телеграмма<br>
avatar - Аватар<br>
tg_chat_id - Телеграм chat-id<br>



## Запуск сервера:
В терминале выполните:
 ```
python manage.py runserver
 ```
Для остановки нажмите Ctrl + C



 ## Тестирование:
Проект покрыт тестами фреймворка DRF. Для их запуска выполните команду:
```
python manage.py test
или
coverage run manage.py test
```
Для выгрузки отчета о покрытии проекта тестами выполните команду:
```
coverage report
или
coverage html
```

## Документация:
http://localhost:8000/swagger/
или
http://localhost:8000/redoc/

## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).
