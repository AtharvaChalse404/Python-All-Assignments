# To add an image field to the employee model in your Django app and display it on the employee details page using HTML card tags, you need to follow these steps:

# Add an image field to the Employee model.
# Update the HTML template to display the employee details including the uploaded photo.
# Let's assume you have an existing Employee model in your Django app. Here's how you can add the image field and update the template:

# In your employee/models.py file:

# python

# from django.db import models

# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
# Make sure to run python manage.py makemigrations and python manage.py migrate after making changes to the model to apply them to the database.

# Now, let's update the employee details template (employee_details.html) to display the employee details including the photo:

# html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Employee Details</title>
#     <style>
#         .card {
#             border: 1px solid #ccc;
#             border-radius: 8px;
#             padding: 16px;
#             margin: 16px;
#             width: 300px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         }

#         .card img {
#             width: 100%;
#             border-radius: 8px;
#         }
#     </style>
# </head>
# <body>
#     <div class="card">
#         <h2>Employee Details</h2>
#         <p><strong>Name:</strong> {{ employee.first_name }} {{ employee.last_name }}</p>
#         <p><strong>Email:</strong> {{ employee.email }}</p>
#         {% if employee.photo %}
#             <img src="{{ employee.photo.url }}" alt="Employee Photo">
#         {% else %}
#             <p>No photo available</p>
#         {% endif %}
#     </div>
# </body>
# </html>
# Make sure to replace employee.first_name, employee.last_name, employee.email, and employee.photo with the appropriate context variables you pass from your view.

# With these changes, your Employee model now has a photo field, and the employee details page will display the employee's photo along with their other details in an HTML card format. Make sure to handle file uploads correctly in your Django settings, including configuring media settings for storing uploaded images.