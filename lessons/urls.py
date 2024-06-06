from django.urls import path
from rest_framework.routers import DefaultRouter

from lessons.apps import LessonsConfig
from lessons.views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateAPIView, SubscriptionView)

app_name = LessonsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson_list/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson_detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
                  path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('subscription/', SubscriptionView.as_view(), name='subscription'),

              ] + router.urls
