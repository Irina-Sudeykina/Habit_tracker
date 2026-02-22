from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit, Reminder
from habits.paginators import CastomPaginator
from habits.serializers import HabitSerializer, ReminderSerializer
from users.permissions import isOwner


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, isOwner)
    pagination_class = CastomPaginator


class HabitPublishedListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    permission_classes = (AllowAny,)
    pagination_class = CastomPaginator


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, isOwner)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, isOwner)


class HabitDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, isOwner)


class ReminderCreateAPIView(CreateAPIView):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit_pk = self.request.data.get("habit")  # получаем PK привычки из тела запроса
        habit = Habit.objects.get(pk=habit_pk)  # находим привычку по этому PK
        serializer.save(owner=self.request.user, habit=habit)  # сохраняем связь


class ReminderListAPIView(ListAPIView):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = (IsAuthenticated, isOwner)
    pagination_class = CastomPaginator


class ReminderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = (IsAuthenticated, isOwner)


class ReminderUpdateAPIView(UpdateAPIView):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = (IsAuthenticated, isOwner)


class ReminderDestroyAPIView(DestroyAPIView):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = (IsAuthenticated, isOwner)
