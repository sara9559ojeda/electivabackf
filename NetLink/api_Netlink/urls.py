from django.urls import path
from .views import PublicacionView

urlpatterns = [
    path('publicacion_list', PublicacionView.as_view())
]
