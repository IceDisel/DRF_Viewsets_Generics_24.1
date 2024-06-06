from users.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Course, Lesson, Subscription


class APITestSetup(APITestCase):
    def setUp(self):
        # Создаем тестовых пользователей
        self.user = User.objects.create(email='testuser@mail.com', password='testpass')

        # Создаем тестовый курс
        self.course = Course.objects.create(title='Test Course', description='Course Description', owner=self.user)

        # Создаем тестовый урок
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Lesson Content', course=self.course,
                                            owner=self.user)

        # Создаем API клиент
        self.client = APIClient()


class LessonCRUDTests(APITestSetup):
    def test_create_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/lessons/lesson_create/',
                                    {'title': 'New Lesson', 'description': 'New Content', 'course': self.course.id},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_get_lessons(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/lessons/lesson_list/')
        # Получение объектов Lesson
        lessons = Lesson.objects.all()

        # Перебор каждого объекта и вывод поля owner
        for lesson in lessons:
            print(f'---{lesson.owner}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f'/lessons/lesson_update/{self.lesson.id}/',
                                   {'title': 'Updated Lesson', 'description': 'Updated Content',
                                    'course': self.course.id},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Lesson')

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/lessons/lesson_delete/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)


class SubscriptionTests(APITestSetup):
    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/lessons/subscription/', {'course_id': self.course.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_unsubscribe_from_course(self):
        self.client.force_authenticate(user=self.user)
        self.client.post('/lessons/subscription/', {'course_id': self.course.id}, format='json')
        response = self.client.post('/lessons/subscription/', {'course_id': self.course.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 0)

    def test_get_course_with_subscription_status(self):
        self.client.force_authenticate(user=self.user)
        self.client.post('/lessons/subscription/', {'course_id': self.course.id}, format='json')
        response = self.client.get(f'/lessons/course/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_subscribed'])
