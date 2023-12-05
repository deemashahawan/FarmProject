Firstly, Farm Project is a web application for managing an animal farm,using django framework.

(models.py):As the first step in this project I built modles(Animal,Feed,Employee,AnimalType) Taking into account the foreign key, relationships (one-to-one, one-to-many, and many-to-many)

(views.py):Then I moved on to building the views page, where it is essentially Python functions or classes that define the logic for a particular page or functionality within a web application ,So , I built a function to list the all contents of each model, in addition to the CRUD Operation for each model.

Regardless, this method worked, but it did not follow the rules of clean code, as many functions performed the same task in different forms, so there was a lot of duplicate code, so I did something more general, so that the code was written once for each form.In other words, one function to list all the contents of the modules, one function to add to all modules, one function to update, and one function to delete from all modules.
After that, I noticed that there is a great similarity between the add function and the update function, except for the presence of a line that checks the presence of the id .So I made them one function, sending id when it is function to update.

(urls.py):the urls.py file is a crucial component in Django for defining how URLs are mapped to views, promoting modularity, readability, and maintainability in your web application.

templates:This folder belongs to the frontand I built the screens with some html,css ,So I can try the application easily.

(api.py):In the end, I converted the code written in the views to the same existing logic to rest-API ,Sometimes the frontend is not ready or we do not even know what it is exactly, so we resort to building the application in this way to bring back Jason file.Or when we build Rest-API, then we can build MobileApp, Web, and Desktop, all of which use the same api .

def safe_json_response(data, status=200):The purpose of this function is to create a JSON response using Django's JsonResponse but with additional handling for cases where the data might not be directly serializable to JSON.

def animal_list(request):The overall purpose of the animal_list function is to provide a JSON response containing information about all animals in the database. It takes advantage of the safe_json_response utility to handle serialization issues and respond gracefully even if the data is complex or includes non-serializable objects.

def add_animal(request):The primary purpose of this view is to handle incoming 'POST' requests containing JSON data to add a new animal to the database.
It is designed to handle potential errors, such as invalid data or integrity violations, and respond with appropriate error messages and status codes.

Decorator: @csrf_exempt This decorator is used to exempt the view from the CSRF (Cross-Site Request Forgery) protection. CSRF protection is a security feature in Django that prevents unauthorized forms from being submitted on behalf of a user.

def delete_animal(request, animal_id):this view allows you to delete an animal by sending a POST request to the endpoint with the corresponding animal ID. The response will contain a JSON message indicating the success of the deletion.






