
Shift Mananger
=====

Quick start
-----------

1. Add "Shifts" to your INSTALLED_APPS setting like this::

~~~
    INSTALLED_APPS = [
        ...
        'shift_mananger',
    ]

~~~

2. Include the polls URLconf in your project urls.py like this::

~~~
    path('shift/', include('shift_mananger.urls')),
~~~

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/shift/ to participate in the poll.