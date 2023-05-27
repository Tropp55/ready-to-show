from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
        path('', views.index, name='index'),
        path('basket', views.basket, name='basket'),
        path('catalog', views.catalog, name='catalog'),
        path('take', views.take, name='take'),
        path('getby', views.getby, name='getby'),
        path('category', views.category, name='category'),
        path('sport', views.sport, name='sport'),
        path('child', views.child, name='child'),
        path('cloth', views.cloth, name='cloth'),
        path('other', views.other, name='other'),
        path('rest', views.rest, name='rest'),
        path('register/', RegisterView.as_view(), name='register'),
]
