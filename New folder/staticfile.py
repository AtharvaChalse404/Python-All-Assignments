# Outer Links:
# Bootstrap: https://getbootstrap.com/docs/5.1/getting-started/download/

# Import necessary modules
import os

# Define the Django project and app name
PROJECT_NAME = 'myproject'
APP_NAME = 'myapp'

# Define the directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, APP_NAME, 'static')
CSS_DIR = os.path.join(STATIC_DIR, 'css')
JS_DIR = os.path.join(STATIC_DIR, 'js')
FONTS_DIR = os.path.join(STATIC_DIR, 'fonts')

# Create the Django project and app
os.system(f'django-admin startproject {PROJECT_NAME}')
os.chdir(PROJECT_NAME)
os.system(f'python manage.py startapp {APP_NAME}')

# Create static directories
os.makedirs(STATIC_DIR)
os.makedirs(CSS_DIR)
os.makedirs(JS_DIR)
os.makedirs(FONTS_DIR)

# Download Bootstrap and extract files
# Copy bootstrap.min.css from the downloaded Bootstrap to static/css directory

# Your bootstrap.min.css file path
BOOTSTRAP_CSS_PATH = '/path/to/bootstrap.min.css'

# Copy bootstrap.min.css to static/css directory
import shutil
shutil.copy(BOOTSTRAP_CSS_PATH, CSS_DIR)

# Output success message
print("Bootstrap CSS file copied successfully to the static/css directory.")
