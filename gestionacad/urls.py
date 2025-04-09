"""
URL configuration for gestionacad project.


    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestcotes import views  # Importer les vues depuis l'application gestcotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/etudiants/', views.etudiants_list_api, name='etudiants-list'),  # GET pour récupérer la liste
    path('api/etudiants/create/', views.etudiants_create_api, name='etudiants-create'),  # POST pour créer un étudiant
    path('api/cours/', views.cours_list_api, name='cours-list'),
    path('api/cotes/', views.cote_list_api, name='cotes-list'),
    path('etudiants/', views.etudiants_list, name='etudiants-list'),
]



    
   
