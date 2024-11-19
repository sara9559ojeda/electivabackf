from django.urls import path
from .views import laboralInformationApiView, academicInformationApiView, experienceApiView, UsuariosView, UsuarioQueryApiView, validateApiView, ExpLaboralAPiView, lastExperienceApiView, AbilityLaboralApiView

urlpatterns=[
    path('login', validateApiView.as_view()),

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

    path('LaboralInfoUpdateApiView/<int:pkid>', laboralInformationApiView.as_view()),
    path('ExpLaboralAPiView/<int:pkid>', ExpLaboralAPiView.as_view()),
    path('lastExperienceApiView/<int:pkid>', lastExperienceApiView.as_view()),
    path('AbilityLaboralApiView/<int:pkid>', AbilityLaboralApiView.as_view()),
    


    path('list', UsuariosView.as_view()),
    path('crear-usuario', UsuariosView.as_view()),
    path ('actualizar-usuario/<int:pkid>', UsuariosView.as_view(), name="actulizar_usuario"),
    path ('eliminar-usuario/<int:pkid>', UsuariosView.as_view(), name="eliminar_usuario"),
    path ('consultar/<int:pkid>', UsuarioQueryApiView.as_view(), name ="consultar"),
]