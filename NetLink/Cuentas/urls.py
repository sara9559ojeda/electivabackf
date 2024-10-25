from django.urls import path
from .views import laboralInformationApiView, academicInformationApiView

urlpatterns=[
    path('Llist', laboralInformationApiView.as_view()),
    path('getLinfo', laboralInformationApiView.as_view()),
    path('laboralInfoAdd', laboralInformationApiView.as_view()),
    path('addPreviousExperiences/<int:pkid>', laboralInformationApiView.as_view()),
    path('addAbility/<int:pkid>', laboralInformationApiView.as_view()),
    path('laboralInfoDelete/<int:pkid>', laboralInformationApiView.as_view()),
]