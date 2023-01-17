
from django.urls import path

from . import views

urlpatterns = [
    path('/<int:series_id>/<int:number_id>', views.about, name='about'),
    path('/made_cards', views.made_some_cards, name='card_gen'),
    path('', views.index, name='index'),
]

