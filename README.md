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


### Контроллер UserCreateAPIView(CreateAPIView) ###
Контроллер для для добавления пользователей


### Модель Habit: ###
Модель представляет привычки, и имеет следующие свойства:<br>
owner - Пользователь<br>
location - Место<br>
time_habit - Время<br>
action_habit - Действие<br>
is_pleasant - Признак приятной привычки<br>
linked_habit - Связанная привычка<br>
frequency - Периодичность<br>
reward - Вознаграждение<br>
time_to_complete - Время на выполнение<br>
is_published - Признак публичности<br>


### Модель Reminder: ###
Модель представляет напоминания, и имеет следующие свойства:<br>
owner - Пользователь<br>
habit - Привычка<br>
date_reminder - Дата напоминания<br>


### Контроллер HabitCreateAPIView(CreateAPIView) ###
Контроллер для создания привычек

### Контроллер HabitListAPIView(ListAPIView) ###
Контроллер для просмотра списка привычек

### Контроллер HabitPublishedListAPIView(ListAPIView) ###
Контроллер для просмотра списка публичных привычек

### Контроллер HabitRetrieveAPIView(RetrieveAPIView) ###
Контроллер для просмотра конкретной привычки

### Контроллер HabitUpdateAPIView(UpdateAPIView) ###
Контроллер для редактирования привычки

### Контроллер HabitDestroyAPIView(DestroyAPIView) ###
Контроллер для удаления привычки


### Контроллер ReminderCreateAPIView(CreateAPIView) ###
Контроллер для создания напоминания

### Контроллер ReminderListAPIView(ListAPIView) ###
Контроллер для просмотра списка напоминаний

### Контроллер ReminderRetrieveAPIView(RetrieveAPIView) ###
Контроллер для просмотра конкретного напоминания

### Контроллер ReminderUpdateAPIView(UpdateAPIView) ###
Контроллер для редактирования напоминания

### Контроллер ReminderDestroyAPIView(DestroyAPIView) ###
Контроллер для удаления напоминания


## Функции:

### Функция send_telegram_message(chat_id, message) ###
Отправляет сообщение в телеграмм<br>
Принимает: <br>
 chat_id - чат id<br>
 message - текст сообщения<br>


## Задачи:

### Задача send_reminder() ###
Периодическая задача для рассылки напоминаний


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
