from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitPublishedListAPIView,
                          HabitRetrieveAPIView, HabitUpdateAPIView, ReminderCreateAPIView, ReminderDestroyAPIView,
                          ReminderListAPIView, ReminderRetrieveAPIView, ReminderUpdateAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("published/", HabitPublishedListAPIView.as_view(), name="published_list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_detete"),
    path("reminders/create/", ReminderCreateAPIView.as_view(), name="reminder_create"),
    path("reminders/", ReminderListAPIView.as_view(), name="reminder_list"),
    path("reminders/<int:pk>/", ReminderRetrieveAPIView.as_view(), name="reminder_detail"),
    path("reminders/<int:pk>/update/", ReminderUpdateAPIView.as_view(), name="reminder_update"),
    path("reminders/<int:pk>/delete/", ReminderDestroyAPIView.as_view(), name="reminder_detete"),
]
