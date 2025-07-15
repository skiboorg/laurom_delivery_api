from rest_framework import exceptions, serializers, status, generics


from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class NewsItemShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        exclude = ['content_editor','content']


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = NewsItem
        fields = '__all__'











