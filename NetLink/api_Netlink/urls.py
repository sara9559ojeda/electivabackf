from django.urls import path
from .views import PublicacionView

urlpatterns = [
    path('list', PublicacionView.as_view())
]
