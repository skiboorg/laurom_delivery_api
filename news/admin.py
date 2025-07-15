from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.safestring import mark_safe
from .models import *

class ImageInline(NestedStackedInline):
    model = Image
    extra = 0


class NewsItemAdmin(NestedModelAdmin):
    model = NewsItem
    inlines = [ImageInline]

admin.site.register(NewsItem, NewsItemAdmin)