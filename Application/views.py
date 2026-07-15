from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, AppointmentForm, DoctorForm

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def patients(request):
    q = request.GET.get('q')
    if q:
        data = Patient.objects.filter(name__icontains=q)
    else:
        data = Patient.objects.all()
    return render(request, "patients.html", {'patients': data})

@login_required
def add_patient(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    return render(request, "add_patient.html", {'form': form})

@login_required
def edit_patient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    return render(request, "edit_patient.html", {'form': form})

@login_required
def delete_patient(request, id):
    Patient.objects.get(id=id).delete()
    return redirect('patients')

@login_required
def doctors(request):
    q = request.GET.get('q')
    if q:
        data = Doctor.objects.filter(name__icontains=q)
    else:
        data = Doctor.objects.all()
    return render(request, "doctors.html", {'doctors': data})

@login_required
def add_doctor(request):
    form = DoctorForm()
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    return render(request, "add_doctor.html", {'form': form})

@login_required
def toggle_doctor(request, id):
    d = Doctor.objects.get(id=id)
    d.available = not d.available
    d.save()
    return redirect('doctors')

@login_required
def appointment(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history')
    return render(request, "appointment.html", {'form': form})

@login_required
def history(request):
    data = Appointment.objects.all()
    return render(request, "history.html", {'history': data})

@login_required
def edit_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doctor)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    return render(request, 'edit_doctor.html', {'form': form})

@login_required
def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect('doctors')

