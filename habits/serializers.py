from rest_framework import serializers
from habits.models import Habit
from habits.validators import (
    validate_linked_habit_and_reward,
    validate_time_to_complete,
    validate_linked_habit_is_pleasant,
    validate_pleasant_habit_no_rewards_or_links,
    validate_frequency
)


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[validate_time_to_complete])
    frequency = serializers.IntegerField(validators=[validate_frequency])

    def validate(self, data):
        # Общий валидатор для всех полей
        instance = self.instance or Habit(**data)

        # Здесь подключаем все наши валидаторы последовательно
        validate_linked_habit_and_reward(instance)
        validate_linked_habit_is_pleasant(instance)
        validate_pleasant_habit_no_rewards_or_links(instance)

        return data

    class Meta:
        model = Habit
        fields = "__all__"
