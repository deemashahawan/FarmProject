from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal,AnimalType,Feed,Employee
from .forms import AnimalForm,AnimalTypeForm,FeedForm,EmployeeForm 



# Create your views here.
def index(req):
    x={'name':'deema',
       'age':21}
    return render(req,'farm/index.html',x)

#def employee(req):
    #return render(req,'farm/employee.html')

#def animal(req):
    #return render(req,'farm/animal.html')

#def animaltype(req):
    #return render(req,'farm/animaltype.html')

#def feed(req):
    #return render(req,'farm/feed.html')

def animal_list(request):
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'farm/animal.html', context)

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    context = {'form': form}
    return render(request, 'farm/animal_form.html', context)

def update_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    context = {'form': form, 'animal': animal}
    return render(request, 'farm/animal_form.html', context)

def delete_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    animal.delete()
    return redirect('animal_list')
##################
def animal_type_list(request):
    animal_types = AnimalType.objects.all()
    context = {'animal_types': animal_types}
    return render(request, 'farm/animaltype.html', context)

def add_animal_type(request):
    if request.method == 'POST':
        form = AnimalTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_type_list')
    else:
        form = AnimalTypeForm()
    context = {'form': form}
    return render(request, 'farm/animaltype_form.html', context)

def delete_animal_type(request, animal_type_id):
    animal_type = AnimalType.objects.get(id=animal_type_id)
    animal_type.delete()
    return redirect('animal_type_list')

###########
def feed_list(request):
    feeds = Feed.objects.all()
    context = {'feeds': feeds}
    return render(request, 'farm/feed.html', context)

def add_feed(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_list')
    else:
        form = FeedForm()
    context = {'form': form}
    return render(request, 'farm/feed_form.html', context)

def delete_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    feed.delete()
    return redirect('feed_list')

##################
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'farm/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'farm/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'farm/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'farm/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'farm/employee_confirm_delete.html', {'employee': employee})