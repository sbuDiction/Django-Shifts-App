from django import forms

WEEK_DAYS = (
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
)


class NameForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    # select = forms.ChoiceField(choices=WEEK_DAYS)
    days = forms.MultipleChoiceField(choices=WEEK_DAYS, widget=forms.CheckboxSelectMultiple)


