from django.shortcuts import  get_object_or_404
from django.http import JsonResponse
from .models import Animal, AnimalType, Feed, Employee


def animal_list(request):
    animals = Animal.objects.values()
    return JsonResponse({'animals': list(animals)})

def add_animal(request):
    if request.method == 'POST':
        data = request.POST
        animal = Animal.objects.create(
            name=data.get('name'),
            type_id=data.get('type'),
            gender=data.get('gender'),
            weight=data.get('weight')
        )
        animal.feeds.set(data.getlist('feeds'))
        return JsonResponse({'animal_id': animal.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def update_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        data = request.POST
        animal.name = data.get('name')
        animal.type_id = data.get('type')
        animal.gender = data.get('gender')
        animal.weight = data.get('weight')
        animal.feeds.set(data.getlist('feeds'))
        animal.save()
        return JsonResponse({'message': 'Animal updated successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    animal.delete()
    return JsonResponse({'message': 'Animal deleted successfully'})
##############################
def animal_type_list(request):
    animal_types = AnimalType.objects.values()
    return JsonResponse({'animal_types': list(animal_types)})

def add_animal_type(request):
    if request.method == 'POST':
        data = request.POST
        animal_type = AnimalType.objects.create(name=data.get('name'))
        return JsonResponse({'animal_type_id': animal_type.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def delete_animal_type(request, animal_type_id):
    animal_type = get_object_or_404(AnimalType, id=animal_type_id)
    animal_type.delete()
    return JsonResponse({'message': 'Animal type deleted successfully'})
###############################
def feed_list(request):
    feeds = Feed.objects.values()
    return JsonResponse({'feeds': list(feeds)})

def add_feed(request):
    if request.method == 'POST':
        data = request.POST
        feed = Feed.objects.create(name=data.get('name'), amount=data.get('amount'))
        return JsonResponse({'feed_id': feed.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def delete_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    feed.delete()
    return JsonResponse({'message': 'Feed deleted successfully'})
###########################
def employee_list(request):
    employees = Employee.objects.values()
    return JsonResponse({'employees': list(employees)})

def employee_create(request):
    if request.method == 'POST':
        data = request.POST
        employee = Employee.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            position=data.get('position')
        )
        return JsonResponse({'employee_id': employee.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        data = request.POST
        employee.first_name = data.get('first_name')
        employee.last_name = data.get('last_name')
        employee.position = data.get('position')
        employee.save()
        return JsonResponse({'message': 'Employee updated successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return JsonResponse({'message': 'Employee deleted successfully'})