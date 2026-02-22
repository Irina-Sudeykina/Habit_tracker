from datetime import timedelta

import pytz
from celery import shared_task
from django.utils import timezone

from habits.models import Habit, Reminder
from habits.servises import send_telegram_message


@shared_task
def send_reminder():
    today = timezone.now().today().date()
    reminders = Reminder.objects.filter(owner__isnull=False, date_reminder=today)

    now = timezone.now()
    next_check_time = now + timedelta(minutes=15)

    local_tz = pytz.timezone("Asia/Yekaterinburg")
    local_now = now.astimezone(local_tz)
    local_next_check_time = next_check_time.astimezone(local_tz)

    for reminder in reminders:
        habits = Habit.objects.filter(
            id=reminder.habit.id, time_habit__gte=local_now.time(), time_habit__lte=local_next_check_time.time()
        )
        print(f"local_now: {local_now.time()} - local_next_check_time: {local_next_check_time.time()}")

        if habits.exists():
            habit = habits.first()  # Берем первый элемент из полученного набора
            message = f"Напоминание: пришло время выполнить привычку '{habit.action_habit}'."
            send_telegram_message(reminder.owner.tg_chat_id, message)
            reminder.date_reminder += timedelta(days=habit.frequency)
            reminder.save()
            print(f"time_habit: {habit.time_habit}")
            print(f"local_next_check_time: {local_next_check_time.time()}")
            print(f"date_reminder: {reminder.date_reminder}")
