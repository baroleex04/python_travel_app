from django.shortcuts import render, get_object_or_404
from .models import Dish, Address

# Create your views here.
def index(request):
    last_five_dishes = Dish.objects.order_by("-add_date")[:5]
    context = {
        "last_five_dishes": last_five_dishes
    }
    return render(request, "travel/index.html", context)

def detail(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    context = {
        "dish": dish
    }
    return render(request, "travel/detail.html", context)