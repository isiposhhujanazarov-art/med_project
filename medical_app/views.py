from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def location_view(request):
    return render(request, 'location.html')

def services_view(request):
    return render(request, 'services.html')

def doctors_view(request):
    return render(request, 'doctors.html')






    from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vrachi, Hospital, Polyklinika, Patient, PoseheniePolik
from .forms import VrachiForm, HospitalForm, PolyklinikaForm, PatientForm, PoseheniePolikForm


def index(request):
    return render(request, 'home.html')


# ================= 1. ВРАЧИ (CRUD) =================
class VrachiListView(ListView):
    model = Vrachi
    template_name = 'crud/vrachi_list.html'
    context_object_name = 'items'

class VrachiDetailView(DetailView):
    model = Vrachi
    template_name = 'crud/vrachi_detail.html'
    context_object_name = 'item'

class VrachiCreateView(CreateView):
    model = Vrachi
    form_class = VrachiForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('vrachi_list')
    extra_context = {'title': 'Добавить врача', 'back_url': 'vrachi_list'}

class VrachiUpdateView(UpdateView):
    model = Vrachi
    form_class = VrachiForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('vrachi_list')
    extra_context = {'title': 'Редактировать врача', 'back_url': 'vrachi_list'}

class VrachiDeleteView(DeleteView):
    model = Vrachi
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('vrachi_list')
    extra_context = {'back_url': 'vrachi_list'}


# ================= 2. БОЛЬНИЦЫ (CRUD) =================
class HospitalListView(ListView):
    model = Hospital
    template_name = 'crud/hospital_list.html'
    context_object_name = 'items'

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'crud/hospital_detail.html'
    context_object_name = 'item'

class HospitalCreateView(CreateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('hospital_list')
    extra_context = {'title': 'Добавить больницу', 'back_url': 'hospital_list'}

class HospitalUpdateView(UpdateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('hospital_list')
    extra_context = {'title': 'Редактировать больницу', 'back_url': 'hospital_list'}

class HospitalDeleteView(DeleteView):
    model = Hospital
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('hospital_list')
    extra_context = {'back_url': 'hospital_list'}


# ================= 3. ПОЛИКЛИНИКИ (CRUD) =================
class PolyklinikaListView(ListView):
    model = Polyklinika
    template_name = 'crud/polyklinika_list.html'
    context_object_name = 'items'

class PolyklinikaDetailView(DetailView):
    model = Polyklinika
    template_name = 'crud/polyklinika_detail.html'
    context_object_name = 'item'

class PolyklinikaCreateView(CreateView):
    model = Polyklinika
    form_class = PolyklinikaForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('polyklinika_list')
    extra_context = {'title': 'Добавить поликлинику', 'back_url': 'polyklinika_list'}

class PolyklinikaUpdateView(UpdateView):
    model = Polyklinika
    form_class = PolyklinikaForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('polyklinika_list')
    extra_context = {'title': 'Редактировать поликлинику', 'back_url': 'polyklinika_list'}

class PolyklinikaDeleteView(DeleteView):
    model = Polyklinika
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('polyklinika_list')
    extra_context = {'back_url': 'polyklinika_list'}


# ================= 4. ПАЦИЕНТЫ (CRUD) =================
class PatientListView(ListView):
    model = Patient
    template_name = 'crud/patient_list.html'
    context_object_name = 'items'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'crud/patient_detail.html'
    context_object_name = 'item'

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('patient_list')
    extra_context = {'title': 'Добавить пациента', 'back_url': 'patient_list'}

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('patient_list')
    extra_context = {'title': 'Редактировать пациента', 'back_url': 'patient_list'}

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('patient_list')
    extra_context = {'back_url': 'patient_list'}


# ================= 5. ПОСЕЩЕНИЯ ПОЛИКЛИНИКИ (CRUD) =================
class PosehenieListView(ListView):
    model = PoseheniePolik
    template_name = 'crud/posehenie_list.html'
    context_object_name = 'items'

class PosehenieDetailView(DetailView):
    model = PoseheniePolik
    template_name = 'crud/posehenie_detail.html'
    context_object_name = 'item'

class PosehenieCreateView(CreateView):
    model = PoseheniePolik
    form_class = PoseheniePolikForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('posehenie_list')
    extra_context = {'title': 'Записать на приём', 'back_url': 'posehenie_list'}

class PosehenieUpdateView(UpdateView):
    model = PoseheniePolik
    form_class = PoseheniePolikForm
    template_name = 'crud/form.html'
    success_url = reverse_lazy('posehenie_list')
    extra_context = {'title': 'Изменить запись на приём', 'back_url': 'posehenie_list'}

class PosehenieDeleteView(DeleteView):
    model = PoseheniePolik
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('posehenie_list')
    extra_context = {'back_url': 'posehenie_list'}