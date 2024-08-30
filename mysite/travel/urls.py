from django.urls import path

from travel.views import index, detail

app_name="travel"
urlpatterns = [
    path("", index, name="index"),
    path("<int:dish_id>/", detail, name='detail')
]