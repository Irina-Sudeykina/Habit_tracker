from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.managers import CustomUserManager
from users.models import User


class RegistrationTestCase(APITestCase):
    def test_user_registration(self):
        """
        Проверка успешной регистрации пользователя
        """
        # Данные для отправки в запросе
        data = {
            "email": "test@example.com",
            "password": "strongpassword123",
            "phone": "+79991234567",
            "tg_nick": "@example_tg",
        }

        response = self.client.post(reverse("users:register"), data=data)

        # Проверяем код статуса HTTP
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем, что пользователь действительно создал запись в БД
        self.assertTrue(User.objects.filter(email="test@example.com").exists())


class LoginTestCase(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя перед началом теста
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
        )

    def test_login_and_get_tokens(self):
        """
        Проверка входящего логина и получения токенов
        """
        login_data = {"email": "testuser@example.com", "password": "testpass123"}

        response = self.client.post(reverse("users:login"), data=login_data)

        # Ожидаемый успех (код 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Убедимся, что получили access и refresh токены
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class StringRepresentationTestCase(APITestCase):
    def setUp(self):
        # Создание экземпляра пользователя для тестирования
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
        )

    def test_string_representation(self):
        """Тестируем строковое представление пользователя"""
        expected_result = str(self.user)
        actual_result = self.user.__str__()
        self.assertEqual(expected_result, self.user.email)
        self.assertEqual(expected_result, actual_result)


class ManagerTests(TestCase):
    def test_manager_raises_value_error_if_no_email(self):
        """Тестирует, что при отсутствии email выбрасывается ValueError."""
        manager = CustomUserManager()
        with self.assertRaises(ValueError):
            manager.create_user(None, "password")


UserModel = get_user_model()  # Получаем модель текущего активного пользователя


class SuperuserCreationTest(TestCase):
    def test_create_superuser_with_valid_arguments(self):
        """
        Проверяет создание суперпользователя с правильными аргументами.
        """
        # Создаём суперпользователя через стандартный интерфейс модели
        superuser = UserModel.objects.create_superuser(email="superuser@example.com", password="supersecretpassword")

        # Проверяем, что полученный пользователь действительно суперпользователь
        self.assertIsInstance(superuser, UserModel)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_without_is_staff_true(self):
        """
        Проверяет возникновение ошибки при неверном значении is_staff=False.
        """
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser(
                email="invalidstaff@example.com", password="invalidemailpassword", is_staff=False
            )

    def test_create_superuser_without_is_superuser_true(self):
        """
        Проверяет возникновение ошибки при неверном значении is_superuser=False.
        """
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser(
                email="invalidsuper@example.com", password="invalidesuperpassword", is_superuser=False
            )
