from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('^$',views.error, name = '404'),
    path('villagers/',views.villagers,name = 'villagers'),
    path('villagers/add/<str:name>/<int:gender>/<int:species>/<str:phrase>/<int:per>/<str:birth>',views.add_villager),
    path('villagers/edit/<str:name>/',views.edit_villager),
    path('villagers/update/<int:id>/<str:name>/<int:gender>/<int:species>/<str:phrase>/<int:per>/<str:birth>',views.update_villager),
    path('villagers/delete/<str:name>/',views.delete_villager),
    path('materials/',views.materials,name = 'materials'),
    path('materials/add/<str:name>/<int:rarity>',views.add_material),
    path('furnitures/',views.furnitures,name = 'furnitures'),
    path('furnitures/add/<str:name>/<int:source>/<int:buy>/<int:sell>/<int:size>/<int:mat1>*<int:num1>/<int:mat2>*<int:num2>/<int:mat3>*<int:num3>/<int:mat4>*<int:num4>/<int:mat5>*<int:num5>/<int:mat6>*<int:num6>/',views.add_furniture,name = 'furnitures'),
    path('islands/',views.islands,name = 'islands'),
    path('museums/',views.museums,name = 'museums'),
]