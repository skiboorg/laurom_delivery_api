from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(NewsItem)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'content',
    )

