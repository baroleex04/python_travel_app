from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import Dish, Address

# Create your views here.
def index(request):
    last_five_dishes = Dish.objects.order_by("-add_date")[:5]
    context = {
        "last_five_dishes": last_five_dishes
    }
    return render(request, "travel/index.html", context)

def detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    address = dish.address_set.first
    context = {
        "dish": dish,
        "address": address
    }
    if (request.GET.get('likebtn')):
        dish.vote_like = F("vote_like")+1
        dish.save()
        return HttpResponseRedirect(reverse("travel:detail", args=(dish.id,)))
    return render(request, "travel/detail.html", context)
