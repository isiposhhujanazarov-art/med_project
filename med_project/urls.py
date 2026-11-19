"""
URL configuration for med_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from medical_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    # 1. Врачи
    path('vrachi/', views.VrachiListView.as_view(), name='vrachi_list'),
    path('vrachi/<int:pk>/', views.VrachiDetailView.as_view(), name='vrachi_detail'),
    path('vrachi/create/', views.VrachiCreateView.as_view(), name='vrachi_create'),
    path('vrachi/<int:pk>/update/', views.VrachiUpdateView.as_view(), name='vrachi_update'),
    path('vrachi/<int:pk>/delete/', views.VrachiDeleteView.as_view(), name='vrachi_delete'),

    # 2. Больницы
    path('hospitals/', views.HospitalListView.as_view(), name='hospital_list'),
    path('hospitals/<int:pk>/', views.HospitalDetailView.as_view(), name='hospital_detail'),
    path('hospitals/create/', views.HospitalCreateView.as_view(), name='hospital_create'),
    path('hospitals/<int:pk>/update/', views.HospitalUpdateView.as_view(), name='hospital_update'),
    path('hospitals/<int:pk>/delete/', views.HospitalDeleteView.as_view(), name='hospital_delete'),

    # 3. Поликлиники
    path('polyclinics/', views.PolyklinikaListView.as_view(), name='polyklinika_list'),
    path('polyclinics/<int:pk>/', views.PolyklinikaDetailView.as_view(), name='polyklinika_detail'),
    path('polyclinics/create/', views.PolyklinikaCreateView.as_view(), name='polyklinika_create'),
    path('polyclinics/<int:pk>/update/', views.PolyklinikaUpdateView.as_view(), name='polyklinika_update'),
    path('polyclinics/<int:pk>/delete/', views.PolyklinikaDeleteView.as_view(), name='polyklinika_delete'),

    # 4. Пациенты
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),

    # 5. Посещения
    path('visits/', views.PosehenieListView.as_view(), name='posehenie_list'),
    path('visits/<int:pk>/', views.PosehenieDetailView.as_view(), name='posehenie_detail'),
    path('visits/create/', views.PosehenieCreateView.as_view(), name='posehenie_create'),
    path('visits/<int:pk>/update/', views.PosehenieUpdateView.as_view(), name='posehenie_update'),
    path('visits/<int:pk>/delete/', views.PosehenieDeleteView.as_view(), name='posehenie_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
