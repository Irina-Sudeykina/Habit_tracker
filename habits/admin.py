from django.contrib import admin

from habits.models import Habit, Reminder


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "action_habit", "time_habit", "location", "is_pleasant", "linked_habit", "reward")
    list_filter = (
        "owner",
        "action_habit",
        "is_pleasant",
    )
    search_fields = (
        "action_habit",
        "location",
    )


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "habit", "date_reminder")
    list_filter = (
        "owner",
        "date_reminder",
    )
    search_fields = (
        "owner",
        "date_reminder",
    )
