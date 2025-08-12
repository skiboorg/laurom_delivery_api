from rest_framework import serializers
from .models import *
from django.conf import settings




class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class PriceCalcItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCalcItem
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)
    faqs = FaqSerializer(many=True, read_only=True)
    price_calc_items = PriceCalcItemSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        exclude = (
           'description_en',
        'description_ru',
        'about_us_en',
        'about_us_ru',
        'name_en',
        'name_ru',
        'category',
        'is_active',
        'order_num',
        )

class ServiceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name','name_slug']

class CategoryShortSerializer(serializers.ModelSerializer):
    services = ServiceShortSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'name',
            'name_slug',
            'description',
            'services'
        ]
class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CaseGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseGalleryImage
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    images = CaseGalleryImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    services = ServiceShortSerializer(many=True, read_only=True)
    class Meta:
        model = Case
        exclude = ['html_content',]

class CaseShortSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Case
        exclude = ['html_content', 'content']

class CallbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackForm
        fields = '__all__'

        # extra_kwargs = {
        #     "name": {"error_messages": {"required": "Имя обязательное поле"}, 'required': True},
        #     'email': {"error_messages": {"required": "Email обязательное поле"},'required': True},
        #     'phone': {"error_messages": {"required": "Телефон обязательное поле"},'required': True},
        #     'file': {'required': False},
        # }