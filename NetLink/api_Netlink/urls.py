from django.urls import path
from .views import laboralInformationApiView

urlpatterns=[
    path('list', laboralInformationApiView.as_view()),
    path('laboralInfoAdd', laboralInformationApiView.as_view())
]