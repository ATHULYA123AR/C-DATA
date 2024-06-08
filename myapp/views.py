from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Signup,Education,Personal,Professional, Medical,Financial,contact
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def signups(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]

        # Check if the username already exists
        if User.objects.filter(username=c).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, "signup.html")


        # Check if the email already exists
        if User.objects.filter(email=b).exists():
            messages.error(request, "Email is already registered. Please use a different email.")
            return render(request, "signup.html")

        try:
            # Create the user
            user = User.objects.create_user(username=c, password=d, email=b)
            user.save()

            # Create the Signup entry
            e = Signup(Full_Name=a, Email=b, Username=c, Password=d, user=user)
            e.save()

            # Log the user in and redirect to success page
            login(request, user)
            return redirect("signup_success")
        except IntegrityError:
            messages.error(request, "An error occurred. Please try again.")
            return render(request, "signup.html")

    return render(request, "signup.html")


def signins(request):
    if request.method == 'POST':
        a = request.POST['name1']
        b = request.POST['name2']
        user = authenticate(request, username=a, password=b)
        if user is not None:
            login(request, user)
            return redirect('inputs')
        else:
            return redirect('signins')
    return render(request, "signin.html")

def form_success(request):
    return render(request, 'success.html')

@login_required
def inputs(request):
    return render(request, "input.html")

def signup_success(request):
    return render(request, "signup_success.html")

def logouts(request):
    logout(request)
    return redirect("index")

@login_required
def education_view(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        h = request.POST["name8"]
        i = request.POST["name9"]

        Education.objects.create(
            user=request.user,
            Schoolname=a,
            Passoutyear1=b,
            Score1=c,
            Ug=d,
            Passoutyear2=e,
            Score2=f,
            Pg=g,
            Passoutyear3=h,
            Score3=i
        )
        return redirect('form_success')
    return render(request, "education.html")


@login_required
def medical_view(request):
    if request.method == 'POST':
        a = request.POST.get('thyroid')
        b = request.POST.get('allergy')
        c = request.POST.get('asthma')
        d = request.POST.get('diabetic')
        e = request.POST.get('bp')
        f = request.POST.get('cholestrol')

        Medical.objects.create(
            user=request.user,thyroid=a,allergy=b,asthma=c,diabetic=d,bp=e,cholestrol=f
        )
        return redirect('form_success')
    return render(request, 'medical.html')


@login_required
def personal_view(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        e = request.POST["name4"]
        Personal.objects.create(
            user=request.user,
            gender=a,
            address=b,
            phone=c,
            pincode=e
        )
        return redirect('form_success')
    return render(request, "personal.html")


@login_required
def professional_view(request):
    if request.method == "POST":
        a = request.POST["n1"]
        b = request.POST["n2"]
        c = request.POST["n3"]
        d = request.POST["n4"]
        e = request.POST["n5"]
        Professional.objects.create(
            user=request.user,
            Aadharnumber=a,
            Pannumber=b,
            Passportnumber=c,
            Licencenumber=d,
            Electionid=e
        )
        return redirect('form_success')
    return render(request, "professional.html")


@login_required
def financial_view(request):
    if request.method == 'POST':
        loan1 = request.POST['name1']
        amount1 = request.POST['name2']
        payment1 = request.POST['name3']
        loan2 = request.POST['name4']
        amount2 = request.POST['name5']
        payment2 = request.POST['name6']
        loan3 = request.POST['name7']
        amount3 = request.POST['name8']
        payment3 = request.POST['name9']
        Financial.objects.create(
            user=request.user,
            loan1=loan1,
            loan2=loan2,
            loan3=loan3,
            amount1=amount1,
            amount2=amount2,
            amount3=amount3,
            payment1=payment1,
            payment2=payment2,
            payment3=payment3
        )
        return redirect('form_success')
    return render(request, 'financial.html')

@login_required
def data_view(request):
    personal_data = Personal.objects.filter(user=request.user)
    educational_data = Education.objects.filter(user=request.user)
    financial_data = Financial.objects.filter(user=request.user)
    professional_data = Professional.objects.filter(user=request.user)
    medical_data = Medical.objects.filter(user=request.user)

    context = {
        'personal_data': personal_data,
        'educational_data': educational_data,
        'financial_data': financial_data,
        'professional_data': professional_data,
        'medical_data': medical_data
    }
    return render(request, 'data.html', context)

@login_required
def education_update(request,id1):
    u = Education.objects.get(id=id1)
    if request.method == 'POST':
        u.Schoolname = request.POST['name1']
        u.Passoutyear1 = request.POST['name2']
        u.Score1 = request.POST['name3']
        u.Ug = request.POST['name4']
        u.Passoutyear2 = request.POST['name5']
        u.Score2 = request.POST['name6']
        u.Pg = request.POST['name7']
        u.Passoutyear3 = request.POST['name8']
        u.Score3 = request.POST['name9']
        u.save()
        return redirect("data_view")
    return render(request, 'education_update.html', {'eupdatekey': u})

@login_required
def education_delete(request,id1):
    u = Education.objects.get(id=id1)
    u.delete()
    return redirect('data_view')

@login_required
def personal_update(request,id2):
    u = Personal.objects.get(id=id2)
    if request.method == 'POST':
        u.gender = request.POST['name1']
        u.address = request.POST['name2']
        u.phone = request.POST['name3']
        u.pincode = request.POST['name4']
        u.save()
        return redirect("data_view")
    return render(request, 'personal_update.html', {'pupdatekey': u})

@login_required
def personal_delete(request,id2):
    u = Personal.objects.get(id=id2)
    u.delete()
    return redirect('data_view')

@login_required
def professional_update(request,id3):
    u = Professional.objects.get(id=id3)
    if request.method == 'POST':
        u.Aadharnumber = request.POST['n1']
        u.Pannumber = request.POST['n2']
        u.Passportnumber = request.POST['n3']
        u.Licencenumber = request.POST['n4']
        u.Electionid = request.POST['n5']
        u.save()
        return redirect("data_view")
    return render(request, 'professional_update.html', {'proupdatekey': u})

@login_required
def professional_delete(request,id3):
    u = Professional.objects.get(id=id3)
    u.delete()
    return redirect('data_view')

@login_required
def medical_update(request,id4):
    u = Medical.objects.get(id=id4)
    if request.method == 'POST':
        u.thyroid = request.POST['name1']
        u.asthma = request.POST['name2']
        u.allergy = request.POST['name3']
        u.diabetic = request.POST['name4']
        u.bp = request.POST['name5']
        u.cholestrol = request.POST['name6']
        u.save()
        return redirect("data_view")
    return render(request, 'medical_update.html', {'selection': u})

@login_required
def medical_delete(request,id4):
    u = Medical.objects.get(id=id4)
    u.delete()
    return redirect('data_view')

@login_required
def financial_update(request,id5):
    u = Financial.objects.get(id=id5)
    if request.method == 'POST':
        u.loan1 = request.POST['name1']
        u.amount1 = request.POST['name2']
        u.payment1 = request.POST['name3']
        u.loan2 = request.POST['name4']
        u.amount2 = request.POST['name5']
        u.payment2 = request.POST['name6']
        u.loan3 = request.POST['name7']
        u.amount3 = request.POST['name8']
        u.payment3 = request.POST['name9']
        u.save()
        return redirect("data_view")
    return render(request, 'financial_update.html', {'fupdatekey': u})

@login_required
def financial_delete(request,id5):
    u = Financial.objects.get(id=id5)
    u.delete()
    return redirect('data_view')

def contact_success(request):
    return render(request,"contact_success.html")


def contacts(request):
    if request.method == "POST":
        n1 = request.POST['name1']
        n2 = request.POST['name2']
        n3 = request.POST['name3']
        n4 = contact(Name=n1, Email=n2, Message=n3)
        n4.save()
        return render(request, "contact_success.html")  # Ensure this template exists
    return render(request, "contact.html")