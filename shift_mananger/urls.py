from django.urls import path
from . import views

app_name = 'shift'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:person_id>/', views.update_shift, name='update_shift'),
]
