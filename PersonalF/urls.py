from django.urls import path

from . import views

urlpatterns = [
    path('', views.StatusLsit.as_view(), name="M-list"),
    path('createb/', views.CreateBudeget.as_view(), name="create-b"),
    path('createm/', views.CreateMoney.as_view(), name="create-m"),
    path('delete/<str:model_name>/<int:pk>', views.ObjDelete.as_view(), name="delete"),
    path('detail/<str:model_name>/<int:pk>', views.Details.as_view(), name="detail"),
    path('update/<str:model_name>/<int:pk>', views.Update.as_view(), name="update"),
]