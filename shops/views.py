from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Plan, Subscription, OrderDetail
# from .forms import CostumeBookUpdate, CommentForm


class PlanListView(generic.ListView):
    model = Plan
    template_name = 'shops/pricing.html'
    context_object_name = 'plans'
