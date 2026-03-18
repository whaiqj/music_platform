from django.urls import path
from .views import playView, downloadView

urlpatterns = [
    path("<int:id>/", playView, name="play"),
    path("<int:id>/download/", downloadView, name="download"),
]