from rest_framework import serializers

from lessons.models import Lesson
from users.models import Payment


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('email', 'phone', 'country')


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
