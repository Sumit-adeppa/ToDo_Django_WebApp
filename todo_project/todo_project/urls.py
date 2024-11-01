from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<int:item_id>/', views.remove, name='remove'),
    path('admin/', admin.site.urls),
]