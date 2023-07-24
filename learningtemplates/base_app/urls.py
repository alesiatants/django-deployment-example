from django.urls import path
from base_app import views
app_name = 'base_app'
urlpatterns = [
    path('', views.index,name="index"),
    path('other/', views.other,name="other"),
    path('relative/', views.relative,name="relative"),
]



