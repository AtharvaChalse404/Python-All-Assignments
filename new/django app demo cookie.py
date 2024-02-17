
# To create a Django app demonstrating cookies and session creation, you need to follow these steps:

# Set up a new Django project.
# Create a Django app within the project.
# Implement views to set and retrieve cookies and session data.
# Create templates to display cookie and session information.
# Here's a basic example:

# First, create a new Django project:

# bash
# 
# django-admin startproject cookie_session_demo
# Then, create a new Django app within the project:

# bash
# 
# cd cookie_session_demo
# python manage.py startapp cookie_session
# Now, let's define the views and templates.

# In cookie_session/views.py:

# python
# 
# from django.shortcuts import render
# from django.http import HttpResponse

# def set_cookie(request):
#     response = HttpResponse("Cookie set!")
#     response.set_cookie('cookie_demo', 'This is a cookie demo')
#     return response

# def show_cookie(request):
#     cookie_value = request.COOKIES.get('cookie_demo')
#     return render(request, 'cookie_session/cookie_template.html', {'cookie_value': cookie_value})

# def set_session(request):
#     request.session['session_demo'] = 'This is a session demo'
#     return HttpResponse("Session set!")

# def show_session(request):
#     session_value = request.session.get('session_demo')
#     return render(request, 'cookie_session/session_template.html', {'session_value': session_value})
# In cookie_session/urls.py:

# python
# 
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('set-cookie/', views.set_cookie, name='set_cookie'),
#     path('show-cookie/', views.show_cookie, name='show_cookie'),
#     path('set-session/', views.set_session, name='set_session'),
#     path('show-session/', views.show_session, name='show_session'),
# ]
# In cookie_session_demo/urls.py:

# python
# 
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cookie-session/', include('cookie_session.urls')),
# ]
# Create two templates in the cookie_session app's templates directory:

# cookie_template.html:

# html
# 
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Cookie Demo</title>
# </head>
# <body>
#     <h1>Cookie Demo</h1>
#     {% if cookie_value %}
#         <p>Cookie Value: {{ cookie_value }}</p>
#     {% else %}
#         <p>No cookie set</p>
#     {% endif %}
# </body>
# </html>
# session_template.html:

# html
# 
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Session Demo</title>
# </head>
# <body>
#     <h1>Session Demo</h1>
#     {% if session_value %}
#         <p>Session Value: {{ session_value }}</p>
#     {% else %}
#         <p>No session set</p>
#     {% endif %}
# </body>
# </html>
# Make sure to include the templates properly in the app's directory structure.

# Finally, run the Django server:

# bash
# 
# python manage.py runserver
# You can access the following URLs to set and view cookies and sessions:

# Set a cookie: http://127.0.0.1:8000/cookie-session/set-cookie/
# View the cookie: http://127.0.0.1:8000/cookie-session/show-cookie/
# Set a session: http://127.0.0.1:8000/cookie-session/set-session/
# View the session: http://127.0.0.1:8000/cookie-session/show-session/