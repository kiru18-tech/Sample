from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.add_db, name='add_db'),
    path('success/', views.success, name='success'),
]
