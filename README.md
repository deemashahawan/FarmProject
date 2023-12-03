Firstly, Farm Project is a web application for managing an animal farm,using django framework.

(models.py):As the first step in this project I built modles(Animal,Feed,Employee,AnimalType) Taking into account the foreign key, relationships (one-to-one, one-to-many, and many-to-many)

(views.py):Then I moved on to building the views page, where it is essentially Python functions or classes that define the logic for a particular page or functionality within a web application ,So , I built a function to list the all contents of each model, in addition to the CRUD Operation for each model.

Regardless, this method worked, but it did not follow the rules of clean code, as many functions performed the same task in different forms, so there was a lot of duplicate code, so I did something more general, so that the code was written once for each form.In other words, one function to list all the contents of the modules, one function to add to all modules, one function to update, and one function to delete from all modules.
After that, I noticed that there is a great similarity between the add function and the update function, except for the presence of a line that checks the presence of the id .So I made them one function, sending id when it is function to update.

(urls.py):the urls.py file is a crucial component in Django for defining how URLs are mapped to views, promoting modularity, readability, and maintainability in your web application.

templates:This folder belongs to the frontand I built the screens with some html,css ,So I can try the application easily.

(api.py):In the end, I converted the code written in the views to the same existing logic to rest-API ,Sometimes the frontend is not ready or we do not even know what it is exactly, so we resort to building the application in this way to bring back Jason file.Or when we build Rest-API, then we can build MobileApp, Web, and Desktop, all of which use the same api .
