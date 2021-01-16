
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('word/', views.word, name='word'),
]

urlpatterns += [
    path('oxford/', views.oxford, name='oxford'),
]
