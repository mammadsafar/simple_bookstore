from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
import mercadopago

from .models import Plan, Subscription, OrderDetail
from .forms import OrderDetailForm


# from .forms import CostumeBookUpdate, CommentForm


class PlanListView(generic.ListView):
    model = Plan
    template_name = 'shops/pricing.html'
    context_object_name = 'plans'


def buy_plan(request, pk):
    # return HttpResponse(pk)
    plan = get_object_or_404(Plan, pk=pk)
    sdk = mercadopago.SDK("ENV_ACCESS_TOKEN")
    payment_data = {
        "transaction_amount": 100,
        "token": 'ff8080814c11e237014c1ff593b57b4d',
        "installments": 1,
        "payer": {
            "type": "customer",
            "id": "123456789-jxOV430go9fx2e"
        }
    }
    payment_response = sdk.payment().create(payment_data)
    print(payment_response)
    payment = payment_response["response"]
    return redirect(payment)


def success_buy(request):
    plan_id = 1
    user_id = 1

    plan_detail = dict()

    plan_detail['user'] = user_id
    plan_detail['plan'] = plan_id
    plan_detail['payment_status'] = True

    form_data = OrderDetailForm(plan_detail)

    if form_data.is_valid():
        form_data.save()

    else:
        return 'Order Detail is not valid'

    return True
