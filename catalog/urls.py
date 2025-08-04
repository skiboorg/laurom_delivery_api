from django.urls import path,include
from . import views



urlpatterns = [
    path('categories', views.CategoryListView.as_view()),
    path('cases', views.CasesListView.as_view()),
    path('case/<name_slug>', views.CaseView.as_view()),
    path('faqs', views.FaqListView.as_view()),
    path('categories/<name_slug>', views.CategoryRetrieveView.as_view()),
    path('service/<name_slug>', views.ServiceRetrieveView.as_view()),
    path('form', views.NewForm.as_view()),
]
