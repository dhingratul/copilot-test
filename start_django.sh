# Start a python3 virtual environment, install django, djangorestframework and start a new project
mkdir expense_calculator
cd expense_calculator
conda create -n expense_calculator python=3.8
conda activate expense_calculator
conda install django
conda install -c conda-forge djangorestframework # Manually added
django-admin startproject expense_calculator .
django-admin startapp expenses
python manage.py runserver

