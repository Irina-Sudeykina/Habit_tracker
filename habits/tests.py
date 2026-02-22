from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, Reminder
from users.models import User


class HabitTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
        )
        self.habit = Habit.objects.create(
            action_habit="Попить воды",
            time_habit="06:00",
            location="дом",
            is_pleasant=False,
            frequency=1,
            reward="Съесть фруктик",
            time_to_complete=50,
            is_published=False,
            owner=self.user    # Назначаем владельца объектом теста
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_detail", kwargs={"pk": self.habit.pk})
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("action_habit"),
            self.habit.action_habit
        )
