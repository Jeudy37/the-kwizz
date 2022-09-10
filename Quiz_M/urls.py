from django.urls import path
from . import views
urlpatterns = [
    path('',views.acceuil, name='acceuil'),
    path('kreyekont/',views.kreyeKont, name='kont'),
    path('konekte/',views.konekte, name='konekte'),
    path('kreyekwiz/',views.kreyekwiz, name='kreyekwiz'),
    path('jwee/',views.jwe, name='jwee'),
    path('dekonekte/',views.dekonekte,name='dekonekte')
]

