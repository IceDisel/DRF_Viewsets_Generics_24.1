from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lessons.models import Course, Lesson


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    # course = CourseSerializers()

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializers(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
