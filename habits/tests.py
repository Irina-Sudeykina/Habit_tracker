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
            owner=self.user,  # Назначаем владельца объектом теста
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_detail", kwargs={"pk": self.habit.pk})
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("action_habit"), self.habit.action_habit)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "action_habit": "Привычка №1",
            "time_habit": "06:00",
            "location": "дом",
            "is_pleasant": True,
            "frequency": 1,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit_update", kwargs={"pk": self.habit.pk})
        data = {"action_habit": "Побыть в тишине"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("action_habit"), "Побыть в тишине")

    def test_habit_delete(self):
        url = reverse("habits:habit_detete", kwargs={"pk": self.habit.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Habit.objects.all().count(), 1)

        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "time_to_complete": 50,
                    "frequency": 1,
                    "location": "дом",
                    "time_habit": "06:00:00",
                    "action_habit": "Попить воды",
                    "is_pleasant": False,
                    "reward": "Съесть фруктик",
                    "is_published": False,
                    "owner": self.user.pk,
                    "linked_habit": None,
                }
            ],
        }

        self.assertEqual(data, result)

    def test_string_representation(self):
        """Тестируем строковое представление привычки"""
        expected_result = str(self.habit)
        actual_result = self.habit.__str__()
        self.assertEqual(expected_result, actual_result)


class ReminderTestCase(APITestCase):

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
            owner=self.user,
        )
        self.reminder = Reminder.objects.create(
            owner=self.user,
            habit=self.habit,
            date_reminder="2026-02-23",
        )
        self.client.force_authenticate(user=self.user)

    def test_reminder_retrieve(self):
        url = reverse("habits:reminder_detail", kwargs={"pk": self.reminder.pk})
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("date_reminder"), self.reminder.date_reminder)

    def test_reminder_create(self):
        url = reverse("habits:reminder_create")
        data = {
            "owner": self.user.pk,
            "habit": self.habit.pk,
            "date_reminder": "2026-02-23",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 2)

    def test_reminder_update(self):
        url = reverse("habits:reminder_update", kwargs={"pk": self.reminder.pk})
        data = {"date_reminder": "2026-02-25"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("date_reminder"), "2026-02-25")

    def test_reminder_delete(self):
        url = reverse("habits:reminder_detete", kwargs={"pk": self.reminder.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Reminder.objects.all().count(), 0)

    def test_reminder_list(self):
        url = reverse("habits:reminder_list")
        response = self.client.get(url)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Reminder.objects.all().count(), 1)

        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": self.reminder.pk, "owner": self.user.pk, "habit": self.habit.pk, "date_reminder": "2026-02-23"}
            ],
        }

        self.assertEqual(data, result)

    def test_string_reminder(self):
        """Тестируем строковое представление напоминания"""
        expected_result = str(self.reminder)
        actual_result = self.reminder.__str__()
        self.assertEqual(expected_result, actual_result)


class HabitValidationTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
        )
        self.habit = Habit.objects.create(
            action_habit="Приятная привычка",
            time_habit="06:00",
            location="дом",
            frequency=1,
            time_to_complete=40,
            is_pleasant=True,
            owner=self.user,
        )
        self.habit_2 = Habit.objects.create(
            action_habit="Полезная привычка",
            time_habit="06:00",
            location="дом",
            frequency=1,
            time_to_complete=40,
            is_pleasant=False,
            reward="Награда",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_validate_linked_habit_and_reward(self):
        url = reverse("habits:habit_create")

        # Создаем привычку, пытаясь задать одновременно связанную привычку и вознаграждение
        data = {
            "action_habit": "Привычка №2",
            "time_habit": "07:00",
            "location": "дом",
            "linked_habit": self.habit.id,
            "reward": "Награда",
            "frequency": 1,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_linked_habit_is_pleasant(self):
        url = reverse("habits:habit_create")

        # Попытка указать полезную привычку в качестве связанной
        data = {
            "action_habit": "Полезная привычка №2",
            "time_habit": "07:00",
            "location": "дом",
            "is_pleasant": False,
            "linked_habit": self.habit_2.id,
            "frequency": 1,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_pleasant_habit_no_rewards_or_links(self):
        url = reverse("habits:habit_create")

        # Попытка для приятной привычки указать вознаграждение
        data = {
            "action_habit": "Приятная привычка",
            "time_habit": "07:00",
            "location": "дом",
            "is_pleasant": True,
            "reward": "Награда",
            "frequency": 1,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Попытка для приятной привычки указать связанную
        data = {
            "action_habit": "Приятная привычка",
            "time_habit": "07:00",
            "location": "дом",
            "is_pleasant": True,
            "linked_habit": self.habit.id,
            "frequency": 1,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_frequency(self):
        url = reverse("habits:habit_create")

        # Попытка указать периодичность выполнения привычки более 7 дней
        data = {
            "action_habit": "Приятная привычка",
            "time_habit": "07:00",
            "location": "дом",
            "is_pleasant": True,
            "frequency": 10,
            "time_to_complete": 40,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_time_to_complete(self):
        url = reverse("habits:habit_create")

        # Попытка указать максимальное время на выполнение привычки более 120 секунд
        data = {
            "action_habit": "Приятная привычка",
            "time_habit": "07:00",
            "location": "дом",
            "is_pleasant": True,
            "frequency": 1,
            "time_to_complete": 300,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class IsOwnerPermissionTest(APITestCase):
    def setUp(self):
        # Создаем двух пользователей
        self.user_owner = User.objects.create_user(
            email="owner@test.com",
            password="testpass123",
        )
        self.user_other = User.objects.create_user(
            email="other@test.com",
            password="testpass123",
        )

        # Создаем привычку, принадлежащую первому пользователю
        self.habit = Habit.objects.create(
            action_habit="Приятная привычка",
            time_habit="06:00",
            location="дом",
            frequency=1,
            time_to_complete=40,
            is_pleasant=True,
            owner=self.user_owner,
        )
        self.url = reverse("habits:habit_detail", kwargs={"pk": self.habit.pk})

    def test_owner_can_access(self):
        """Проверка: владелец имеет доступ"""
        self.client.force_authenticate(user=self.user_owner)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_owner_forbidden(self):
        """Проверка: чужой пользователь получает 403"""
        self.client.force_authenticate(user=self.user_other)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "Вы не являетесь владельцем.")

    def test_anonymous_forbidden(self):
        """Проверка: неавторизованный пользователь получает 403 или 401"""
        response = self.client.get(self.url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
