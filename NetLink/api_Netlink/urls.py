from django.urls import path
from .views import PublicacionView
#url de publicacion
urlpatterns = [
    path('publicacion_list', PublicacionView.as_view()),
    path('publicacion_create', PublicacionView.as_view())
]

