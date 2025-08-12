from django.contrib import admin
from .models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class CaseGalleryImageInline(NestedStackedInline):
    model = CaseGalleryImage
    extra = 0


class CaseAdmin(NestedModelAdmin):
    model = Case
    inlines = [CaseGalleryImageInline]

class PriceCalcItemInline(NestedStackedInline):
    model = PriceCalcItem
    extra = 0

class ServiceAdmin(NestedModelAdmin):
    model = Service
    inlines = [PriceCalcItemInline]


admin.site.register(Category)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Tag)
admin.site.register(Case,CaseAdmin)
admin.site.register(Feature)
admin.site.register(Step)
admin.site.register(Price)
admin.site.register(Faq)
admin.site.register(CallbackForm)




