from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Person, Shift, ShiftForm, User, Days, Workers
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NameForm
from .functions import return_json


# Create your views here.


# class IndexView(generic.ListView):
#     template_name = 'shift_mananger/index.html'
#     context_object_name = 'latest_people_list'

#     def get_queryset(self):
#         return Person.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')

def index(request):
    workers = [{
        'week_day': "Sunday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Monday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Tuesday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Wednesday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Thursday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Friday",
        'counter': 0,
        'workers': []
    }, {
        'week_day': "Saturday",
        'counter': 0,
        'workers': []
    }]

    db_data = Person.objects.all()
    for people_data in db_data:
        each_person = Person.objects.get(pk=people_data.id)
        get_selected = each_person.shift_set.all()
        for person_counter in get_selected:
            for days in workers:
                if person_counter.counter == 1:
                    if str(days['week_day']) == str(person_counter.get_day_display()):
                        days['counter'] += 1
                        days['workers'].append(each_person)
    return render(request, 'shift_mananger/index.html', {
        'latest_people_list': workers,
        'counter': db_data,
        'people': db_data,
    })


class DetailView(generic.DetailView):
    model = Person
    template_name = 'shift_mananger/detail.html'


def update_shift(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    selected_shift = person.shift_set.all()
    form = ShiftForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        days_array = data['days']
        for selected_days in selected_shift:
            selected_days.counter = 0
            selected_days.save()
            for days in days_array:
                if str(days) == str(selected_days):
                    shift_instance = person.shift_set.get(pk=selected_days.id)
                    shift_instance.counter = 1
                    shift_instance.save()

    else:
        shift_instance = person.shift_set.all()
        for days in shift_instance:
            reset_counter = person.shift_set.get(pk=days.id)
            reset_counter.counter = 0
            reset_counter.save()
        return render(request, 'shift_mananger/detail.html', {
            'person': person,
            'clear_message': "You cleared shift",
        })

    return render(request, 'shift_mananger/detail.html', {
        'person': person,
        'success_message': "Updated was successfully",
    })
