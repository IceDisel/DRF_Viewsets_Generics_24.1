from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lessons.models import Course, Lesson, Subscription
from lessons.validators import YouTubeLinkValidator


class CourseSerializers(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'is_subscribed']

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


class LessonSerializers(serializers.ModelSerializer):
    # course = CourseSerializers()

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeLinkValidator(field='video_url')]


class CourseDetailSerializers(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializers(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
