from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal,AnimalType,Feed,Employee
from .forms import AnimalForm,AnimalTypeForm,FeedForm,EmployeeForm 
from django.urls import reverse



# Create your views here.

def list_model(request, model, template_name, context_name):
    items = model.objects.all()
    context = {context_name: items}
    return render(request, template_name, context)

def manage_model(request, model, form_class, item_id=None, template_name=None, list_url=None):
    instance = get_object_or_404(model, id=item_id) if item_id else None

    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(list_url)
    else:
        form = form_class(instance=instance)

    context = {'form': form, 'item': instance}
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
    return manage_model(request,Animal ,AnimalForm,template_name= 'farm/animal_form.html', list_url='animal_list')

def update_animal(request, animal_id):
    return manage_model(request, Animal, AnimalForm, item_id=animal_id,template_name= 'farm/animal_form.html',list_url= 'animal_list')

def delete_animal(request, animal_id):
        return delete_model(request, Animal, animal_id, 'animal_list')
##################
def animal_type_list(request):
    return list_model(request, AnimalType, 'farm/animaltype.html', 'animal_types')

def add_animal_type(request):
    return manage_model(request,AnimalType, AnimalTypeForm, template_name='farm/animaltype_form.html',list_url= 'animal_type_list')

def delete_animal_type(request, animal_type_id):
    return delete_model(request, AnimalType, animal_type_id, 'animal_type_list')

###########
def feed_list(request):
    return list_model(request, Feed, 'farm/feed.html', 'feeds')

def add_feed(request):
    return manage_model(request, Feed, FeedForm,template_name= 'farm/feed_form.html',list_url='feed_list')

def delete_feed(request, feed_id):
    return delete_model(request, Feed, feed_id, 'feed_list')

##################
def employee_list(request):
    return list_model(request, Employee, 'farm/employee_list.html', 'employees')

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'farm/employee_detail.html', {'employee': employee})

def employee_create(request):
    return manage_model(request,Employee, EmployeeForm,template_name= 'farm/employee_form.html',list_url= 'employee_list')

def employee_update(request, pk):
   return manage_model(request, Employee, EmployeeForm,item_id= pk,template_name= 'farm/employee_form.html',list_url='employee_list')

def employee_delete(request, pk):
     return delete_model(request, Employee, pk, 'employee_list')
