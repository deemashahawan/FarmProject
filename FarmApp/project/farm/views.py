from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal,AnimalType,Feed,Employee
from .forms import AnimalForm,AnimalTypeForm,FeedForm,EmployeeForm 
from django.urls import reverse



# Create your views here.

def list_model(request, model, template_name, context_name):
    items = model.objects.all()
    context = {context_name: items}
    return render(request, template_name, context)

def add_model(request, form_class, template_name, list_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_url)
    else:
        form = form_class()
    context = {'form': form}
    return render(request, template_name, context)

def update_model(request, model, form_class, item_id, template_name, list_url):
    item = get_object_or_404(model, id=item_id)
    if request.method == 'POST':
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(list_url)
    else:
        form = form_class(instance=item)
    context = {'form': form, 'item': item}
    return render(request, template_name, context)

def delete_model(request, model, item_id, list_url):
    item = get_object_or_404(model, id=item_id)
    item.delete()
    return redirect(list_url)
###########################################

def index(req):
    links = {
        "animal_list": reverse('animal_list'),
        "animal_type_list": reverse('animal_type_list'),
        "feed_list": reverse('feed_list'),
        "employee_list": reverse('employee_list'),
    }
    return render(req,'farm/index.html', {'links': links})


def animal_list(request):
    return list_model(request, Animal, 'farm/animal.html', 'animals')

def add_animal(request):
    return add_model(request, AnimalForm, 'farm/animal_form.html', 'animal_list')

def update_animal(request, animal_id):
    return update_model(request, Animal, AnimalForm, animal_id, 'farm/animal_form.html', 'animal_list')

def delete_animal(request, animal_id):
        return delete_model(request, Animal, animal_id, 'animal_list')
##################
def animal_type_list(request):
    return list_model(request, AnimalType, 'farm/animaltype.html', 'animal_types')

def add_animal_type(request):
    return add_model(request, AnimalTypeForm, 'farm/animaltype_form.html', 'animal_type_list')

def delete_animal_type(request, animal_type_id):
    return delete_model(request, AnimalType, animal_type_id, 'animal_type_list')

###########
def feed_list(request):
    return list_model(request, Feed, 'farm/feed.html', 'feeds')

def add_feed(request):
    return add_model(request, FeedForm, 'farm/feed_form.html', 'feed_list')

def delete_feed(request, feed_id):
    return delete_model(request, Feed, feed_id, 'feed_list')

##################
def employee_list(request):
    return list_model(request, Employee, 'farm/employee_list.html', 'employees')

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'farm/employee_detail.html', {'employee': employee})

def employee_create(request):
    return add_model(request, EmployeeForm, 'farm/employee_form.html', 'employee_list')

def employee_update(request, pk):
   return update_model(request, Employee, EmployeeForm, pk, 'farm/employee_form.html', 'employee_list')

def employee_delete(request, pk):
     return delete_model(request, Employee, pk, 'employee_list')
