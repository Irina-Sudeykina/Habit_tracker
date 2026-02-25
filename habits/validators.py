from django.core.exceptions import ValidationError


def validate_linked_habit_and_reward(instance):
    """
    Валидатор для исключения одновременного выбора связанной привычки и указания вознаграждения.

    Проверяет, что поля 'linked_habit' и 'reward' не заполнены одновременно.
    Если оба поля заполнены, выбрасывается исключение ValidationError.
    """
    if instance.linked_habit and instance.reward:
        raise ValidationError("Нельзя указывать одновременно связанную привычку и вознаграждение.")


def validate_time_to_complete(value):
    """
    Валидатор ограничения максимального значения поля 'time_to_complete'.
    Ограничение: максимальное значение — 120 секунд.
    """
    if value > 120:
        raise ValidationError("Максимальное время на выполнение привычки — 120 секунд.")


def validate_linked_habit_is_pleasant(instance):
    """
    Валидатор, ограничивающий привязку привычки только к приятным привычкам.
    Связанной привычке обязательно должно соответствовать условие is_pleasant=True.
    """
    if instance.linked_habit and not instance.linked_habit.is_pleasant:
        raise ValidationError("Привычки могут быть связаны только с приятными привычками.")


def validate_pleasant_habit_no_rewards_or_links(instance):
    """
    Валидатор запрещает наличие вознаграждения или связанной привычки у приятных привычек.
    Если привычка отмечена как приятная (is_pleasant=True),
    она не должна иметь вознаграждение или связанную привычку.
    """
    if instance.is_pleasant and (instance.reward or instance.linked_habit):
        raise ValidationError("Приятная привычка не может иметь вознаграждения или связанной привычки.")


def validate_frequency(value):
    """
    Валидатор ограничения максимального значения поля 'frequency'.
    Ограничение: максимальное значение — 7 дней.
    """
    if value > 7:
        raise ValidationError("Максимальная периодичность выполнения привычки — 7 дней.")
