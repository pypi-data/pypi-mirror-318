
Django notification popups app.

### Installation

Install with pip:

```
pip install django-mp-notify
```

Settings:
```
INSTALLED_APPS = [
    ...,
    'notify'
]
```

Using:
```
{% load notify %}

{% block js %}

    ...

    {% notify_js %}

{% endblock %}
```
