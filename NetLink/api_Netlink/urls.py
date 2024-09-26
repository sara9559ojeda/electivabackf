from django.urls import path
from .views import laboralInformationApiView

urlpatterns=[
    path('laboralInfoList', laboralInformationApiView.as_view())
]