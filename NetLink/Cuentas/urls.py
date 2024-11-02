from django.urls import path
from .views import laboralInformationApiView, academicInformationApiView, experienceApiView

urlpatterns=[
    path('Llist', laboralInformationApiView.as_view()),
    path('getLinfo', laboralInformationApiView.as_view()),
    path('laboralInfoAdd', laboralInformationApiView.as_view()),
    path('addPreviousExperiences/<int:pkid>', laboralInformationApiView.as_view()),
    path('addAbility/<int:pkid>', laboralInformationApiView.as_view()),
    path('laboralInfoDelete/<int:pkid>', laboralInformationApiView.as_view()),
    path('getExperiences', experienceApiView.as_view()),
    path('getExperience', experienceApiView.as_view()),
    path('getExperiences', experienceApiView.as_view()),
    path('addExperience', experienceApiView.as_view()),
    path('updateExperience/<int:pkid>', experienceApiView.as_view()),
    path('deleteExperience/<int:pkid>', experienceApiView.as_view()),
]