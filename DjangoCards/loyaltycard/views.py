from .models import Card
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import random
import datetime
from .forms import NameForm


def index(request):
    card_list = Card.objects.all()
    context = {'card_list': card_list}
    return render(request, 'loyaltycard/index.html', context)


def about(request, series_id, number_id):
    card = Card.objects.get(series=series_id, numb=number_id)
    context = {'card': card}
    return render(request, 'loyaltycard/about.html', context)


def made_some_cards(request):
    if request.method == 'POST':  # отправка формы
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cards')
    else:  # первое посещение URL
        form = NameForm()
    return render(request, 'loyaltycard/card_gen.html', {'form': form})



