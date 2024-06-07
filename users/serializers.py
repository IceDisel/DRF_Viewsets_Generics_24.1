from rest_framework import serializers

from lessons.models import Lesson, CoursePayment
from users.models import Payment, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('email', 'phone', 'country')


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePayment
        fields = '__all__'
