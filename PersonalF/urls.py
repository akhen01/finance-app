from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('income/', views.income_setup, name="income"),
    path('budget/', views.budget_setup, name="budget"),
    path('details/', views.details, name="details"),
    path('idelete/<int:id>', views.deleteI, name="idelete"),
    path('gdelete/<int:id>', views.deleteG, name="gdelete"),
    path('details/didelete/<int:id>', views.delete_DI, name="didelete"),
    path('details/dbdelete/<int:id>', views.delete_DG, name="dbdelete"),
    path('status/', views.status, name="status"),
    path('expence/', views.daily_expences, name="expence")
]