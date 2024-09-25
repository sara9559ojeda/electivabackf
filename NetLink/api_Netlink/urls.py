from django.urls import path
from .views import PublicacionView
#url de publicacion
urlpatterns = [
    path('list', PublicacionView.as_view())
]
