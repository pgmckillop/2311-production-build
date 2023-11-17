from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('album/', views.album, name='album'),
    path('detail/<int:project_id>', views.detail, name='detail'),
]