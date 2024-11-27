from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import *
from .forms import VisitorForm
from django.http import JsonResponse

# Create your views here.
def navbar(request):
    return render(request,'navbar.html')
def home(request):
    return render(request,'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'form.html') 
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            messages.error(request, "All fields are required.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')

    return render(request, 'register.html')


def get_buildings(request):
    phase_id = request.GET.get('phase_id')
    buildings = Building.objects.filter(phase_id=phase_id)
    data = [{'id': b.id, 'name': b.name} for b in buildings]
    return JsonResponse(data, safe=False)


def get_companies(request):
    building_id = request.GET.get('building_id')
    companies = Company.objects.filter(building_id=building_id)
    data = [{'id': c.id, 'name': c.name} for c in companies]
    return JsonResponse(data, safe=False)

def visitor_form(request):
    phases = Phase.objects.all()
    form = VisitorForm()
    return render(request, 'visitor_form.html', {'phases': phases, 'form': form})


def submit_visitor_form(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES) 

        if form.is_valid():
            visitor = form.save(commit=False)
            phase_id = request.POST.get('phase')
            building_id = request.POST.get('building')
            company_id = request.POST.get('company')
            visitor.phase = Phase.objects.get(id=phase_id)
            visitor.building = Building.objects.get(id=building_id)
            visitor.company = Company.objects.get(id=company_id)
            visitor.save()

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
               return render(request, 'visitor_id_card.html', {'visitor': visitor})

            return redirect('visitor_id_card', visitor_id=visitor.id)

    return redirect('visitor_form')