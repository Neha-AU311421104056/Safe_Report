
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report 
# Create your views here.
def homepage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'Neha' and password == 'pass@123':
            request.session['is_admin'] = True  # Store login session
            return redirect('showreports')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')


def reportcrime(request):
    """Loads the reportcrime form page"""
    template = loader.get_template("reportcrime.html")
    return HttpResponse(template.render({}, request))

def reportcrime_db(request):
    """Handles report submission and saves to database"""
    if request.method == "POST":
        crime_type = request.POST.get("crime_type")
        location = request.POST.get("location")
        details = request.POST.get("details")
        more_info = request.POST.get("more_info", "")
        crime_datetime = request.POST.get("crime_datetime")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        proof_file = request.FILES.get("proof_files")

        report = Report(
            crime_type=crime_type,
            location=location,
            details=details,
            more_info=more_info,
            crime_datetime=crime_datetime or None,
            latitude=latitude or None,
            longitude=longitude or None,
            proof_files=proof_file,
        )
        report.save()
        return render(request, "reportadded.html")

    return HttpResponse("Invalid Request", status=400)

def showreports(request):
    if not request.session.get('is_admin'):
        return redirect('login')  # Block access if not logged in

    # Fetch crime reports from the database
    reports = Report.objects.all().order_by('-crime_datetime')
    return render(request, 'showreports.html', {'reports': reports})

def reportadded(request):
    template = loader.get_template("reportadded.html")
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

