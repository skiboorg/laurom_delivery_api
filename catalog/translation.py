from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )

@register(Step)
class StepTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
@register(Price)
class PriceTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = (
        'q',
        'a',
    )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'content',
    )

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'about_us',
        'price_calc_title',
        'price_calc_small_title',
    )
@register(PriceCalcItem)
class PriceCalcItemTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

@register(Case)
class CaseTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'content',
    )