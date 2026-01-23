from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet

from users.forms import PatientForm
from users.models import Doctor, Patient
from users.serializers import DoctorSerializer, PatientSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PatientForm()

    return render(request, 'users/patient_form.html', {'form': form})
