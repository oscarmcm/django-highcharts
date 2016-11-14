# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	chart,
	data,
	config,
)


class chartCreateView(CreateView):

    model = chart


class chartDeleteView(DeleteView):

    model = chart


class chartDetailView(DetailView):

    model = chart


class chartUpdateView(UpdateView):

    model = chart


class chartListView(ListView):

    model = chart


class dataCreateView(CreateView):

    model = data


class dataDeleteView(DeleteView):

    model = data


class dataDetailView(DetailView):

    model = data


class dataUpdateView(UpdateView):

    model = data


class dataListView(ListView):

    model = data


class configCreateView(CreateView):

    model = config


class configDeleteView(DeleteView):

    model = config


class configDetailView(DetailView):

    model = config


class configUpdateView(UpdateView):

    model = config


class configListView(ListView):

    model = config

