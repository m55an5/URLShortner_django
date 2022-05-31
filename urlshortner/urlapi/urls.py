from django.urls import path
from .views import CreateURLShortner, GetShortURL

urlpatterns = [
    path('create-short-url/', CreateURLShortner.as_view(), name="create-short-url"),
    path('<str:short_url>', GetShortURL.as_view(), name="get-short-url"),
]