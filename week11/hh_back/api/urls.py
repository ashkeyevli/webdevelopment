from django.urls import path
from api import views


urlpatterns = [
    path('companies/', views.companies),
    path('companies/<int:pk>/', views.company),
    path('companies/<int:pk>/vacancies/', views.company_vacancies),
    path('vacancies/', views.vacancies),
    path('vacancies/<int:pk>', views.vacancy),
    path('vacancies/top_ten/', views.vacancies_top)
]