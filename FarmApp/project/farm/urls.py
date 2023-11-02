from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import  AnimalViewSet, AnimalTypeViewSet, FeedViewSet,EmployeeViewSet 
from django.urls import include


router = DefaultRouter()
router.register(r'animals', AnimalViewSet)
router.register(r'animaltypes', AnimalTypeViewSet)
router.register(r'feeds', FeedViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns=[
    path('',views.index,name='index'),

     #api urls
    path('api/', include(router.urls)), 
    
    path('animals/', views.animal_list, name='animal_list'),
    path('animal/add/', views.add_animal, name='add_animal'),
    path('animal/<int:animal_id>/update/', views.update_animal, name='update_animal'),
    path('animal/<int:animal_id>/delete/', views.delete_animal, name='delete_animal'),

    path('animaltypes/', views.animal_type_list, name='animal_type_list'),
    path('animaltype/add/', views.add_animal_type, name='add_animal_type'),
    path('animaltype/<int:animal_type_id>/delete/', views.delete_animal_type, name='delete_animal_type'),

     path('feeds/', views.feed_list, name='feed_list'),
    path('feed/add/', views.add_feed, name='add_feed'),
    path('feed/<int:feed_id>/delete/', views.delete_feed, name='delete_feed'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
