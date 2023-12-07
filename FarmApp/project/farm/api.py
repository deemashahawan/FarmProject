from django.shortcuts import  get_object_or_404
from django.http import JsonResponse
from .models import Animal, AnimalType, Feed, Employee
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models import Prefetch



SUCCESS_STATUS = 200
ERROR_STATUS = 400
NOT_ALLOWED_STATUS=405

def safe_json_response(data, status=SUCCESS_STATUS):
    try:
        return JsonResponse(data, status=status)
    except TypeError:
        return JsonResponse(json.loads(json.dumps(data, cls=DjangoJSONEncoder)), status=status)

def handle_error_response(error_message, status=ERROR_STATUS):
    return safe_json_response({'error':error_message}, status=status)

def handle_not_allowed_response():
    return safe_json_response({'error': 'Method not allowed'}, status=NOT_ALLOWED_STATUS)


def get_json(request):
    try:
        return json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return None

def validate_and_get_json(request):
    data = get_json(request)
    if data is None:
        return handle_error_response('Invalid JSON format')
    return data

def animal_list(request):
    animals = Animal.objects.prefetch_related(Prefetch('feeds', queryset=Feed.objects.all()))

    animal_data = [
        {
            'id': animal.id,
            'name': animal.name,
            'type_id': animal.type_id,
            'gender': animal.gender,
            'weight': animal.weight,
            'feeds': list(animal.feeds.values('id', 'name'))
        }
        for animal in animals
    ]
    return safe_json_response({'animals':animal_data})

@csrf_exempt
def add_animal(request):
    if request.method == 'POST':
        data = validate_and_get_json(request)
        if data:
            try:
                animal = Animal.objects.create(
                    name=data.get('name'),
                    type_id=data.get('type'),
                    gender=data.get('gender'),
                    weight=data.get('weight')
                )
                animal.feeds.set(data.get('feeds', []))
                return safe_json_response({'animal_id': animal.id})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def update_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        data=validate_and_get_json(request)
        if data:
            try:
                data = json.loads(request.body.decode('utf-8'))
                animal.name = data.get('name')
                animal.type_id = data.get('type')
                animal.gender = data.get('gender')
                animal.weight = data.get('weight')
                animal.feeds.set(data.get('feeds', []))
                animal.save()
                return safe_json_response({'message': 'Animal updated successfully'})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    animal.delete()
    return safe_json_response({'message': 'Animal deleted successfully'})

# AnimalType views
def animal_type_list(request):
    animal_types = AnimalType.objects.values()
    return safe_json_response({'animal_types': list(animal_types)})

@csrf_exempt
def add_animal_type(request):
    if request.method == 'POST':
        data=validate_and_get_json(request)
        if data:
            try:
                data = json.loads(request.body.decode('utf-8'))
                animal_type = AnimalType.objects.create(name=data.get('name'))
                return safe_json_response({'animal_type_id': animal_type.id})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def delete_animal_type(request, animal_type_id):
    animal_type = get_object_or_404(AnimalType, id=animal_type_id)
    animal_type.delete()
    return safe_json_response({'message': 'Animal type deleted successfully'})

# Feed views
def feed_list(request):
    feeds = Feed.objects.values()
    return safe_json_response({'feeds': list(feeds)})

@csrf_exempt
def add_feed(request):
    if request.method == 'POST':
        data=validate_and_get_json(request)
        if data:
            try:
                data = json.loads(request.body.decode('utf-8'))
                feed = Feed.objects.create(name=data.get('name'), amount=data.get('amount'))
                return safe_json_response({'feed_id': feed.id})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def delete_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    feed.delete()
    return safe_json_response({'message': 'Feed deleted successfully'})

# Employee views
def employee_list(request):
    employees = Employee.objects.values()
    return safe_json_response({'employees': list(employees)})

@csrf_exempt
def employee_create(request):
    if request.method == 'POST':
        data=validate_and_get_json(request)
        if data:
            try:
                data = json.loads(request.body.decode('utf-8'))
                employee = Employee.objects.create(
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    position=data.get('position')
                )
                return safe_json_response({'employee_id': employee.id})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        data=validate_and_get_json(request)
        if data:
            try:
                data = json.loads(request.body.decode('utf-8'))
                employee.first_name = data.get('first_name')
                employee.last_name = data.get('last_name')
                employee.position = data.get('position')
                employee.save()
                return safe_json_response({'message': 'Employee updated successfully'})
            except (IntegrityError, ValidationError):
                return handle_error_response('Invalid data provided')
    return handle_not_allowed_response()

@csrf_exempt
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return safe_json_response({'message': 'Employee deleted successfully'})