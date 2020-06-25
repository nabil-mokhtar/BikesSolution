from django.urls import path
from . import views
urlpatterns = [
     path('', views.rent.index, name='rent.index'),
    path('create', views.rent.create, name='rent.create'),
    path('insert',views.rent.insert, name='rent.insert'),
    path('extend/<int:id>',views.rent.extend, name='rent.extend'),
    path('cancel/<int:id>',views.rent.cancel, name='rent.cancel'),

]