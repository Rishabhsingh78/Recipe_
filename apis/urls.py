
from django.urls import path
from home.views import ReceipeApi
urlpatterns = [
    path('receipes/',ReceipeApi.as_view()),
]
