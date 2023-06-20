1. https://github.com/Nokolay0710/Django_quick_start
2. py manage.py startapp newapp
3. cd newapp && mkdir templates
4. create files: base.html, index.html, list.html, add.html
5 Context base.html:

<!-- templates/newapp/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <!-- Include the <meta name="viewport"> tag as well for proper responsive behavior in mobile devices.-->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Include bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  {% block styles %}
  {% endblock %}
  <title>{% block title %}Bootstrap and Django{% endblock %}</title>
</head>
<body>
    <header>
        <!-- Fixed navbar -->
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
            <nav class="my-2 my-md-0 mr-md-3">
                <a class="p-2 text-dark" href="{% url 'index' %}">Home</a>
                <a class="p-2 text-dark" href="{% url 'list' %}">List</a>
                <a class="p-2 text-dark" href="{% url 'add' %}">Add</a>
            </nav>
        </div>
    </header>
    <main>
        {% block sidebar %}
        {% endblock %}
        {% block content %}
        {% endblock %}
    </main>
  <!-- Include Bootstrap Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>

6. Context index.html

{% extends 'base.html' %}

{% load static %}

{% block title %}Index{% endblock title %}

{% block content %}
  <h1>Indexpage</h1>
  <p>Indexpage content.</p>
{% endblock content %}

7. Context list.html

{% extends 'base.html' %}

{% load static %}

{% block title %}List{% endblock title %}

{% block content %}
  <h1>Listpage</h1>
  <p>List content.</p>
{% endblock content %}

8. Context add.html

{% extends 'base.html' %}

{% load static %}

{% block title %}Add{% endblock title %}

{% block content %}
  <h1>Addpage</h1>
  <p>Addpage create content.</p>
{% endblock content %}

9. 

str(BASE_DIR.joinpath('templates'))
