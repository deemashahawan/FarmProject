from django.urls import path
from . import views
from . import api



urlpatterns=[
    path('',views.index,name='index'),
    
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

    path('api/animals/', api.animal_list, name='api_animal_list'),
    path('api/animal/add/', api.add_animal, name='api_add_animal'),
    path('api/animal/<int:animal_id>/update/', api.update_animal, name='api_update_animal'),
    path('api/animal/<int:animal_id>/delete/', api.delete_animal, name='api_delete_animal'),

    path('api/animaltypes/', api.animal_type_list, name='api_animal_type_list'),
    path('api/animaltype/add/', api.add_animal_type, name='api_add_animal_type'),
    path('api/animaltype/<int:animal_type_id>/delete/', api.delete_animal_type, name='api_delete_animal_type'),

    path('api/feeds/', api.feed_list, name='api_feed_list'),
    path('api/feed/add/', api.add_feed, name='api_add_feed'),
    path('api/feed/<int:feed_id>/delete/', api.delete_feed, name='api_delete_feed'),

    path('api/employees/', api.employee_list, name='api_employee_list'),
    path('api/employee/new/', api.employee_create, name='api_employee_create'),
    path('api/employee/<int:pk>/edit/', api.employee_update, name='api_employee_update'),
    path('api/employee/<int:pk>/delete/', api.employee_delete, name='api_employee_delete'),
]
