from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User

from .forms import RegisterForm, ContactForm
from .models import UserProfile, ContactMessage

# صفحه اصلی
def home(request):
    return render(request, 'fitness_app/home.html')


# ثبت‌نام کاربر
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            fitness_level = form.cleaned_data['fitness_level']
            UserProfile.objects.create(user=user, fitness_level=fitness_level)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'fitness_app/register.html', {'form': form})


# ورود کاربر
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'fitness_app/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است'})
    return render(request, 'fitness_app/login.html')


# خروج کاربر
def user_logout(request):
    logout(request)
    return redirect('login')


# داشبورد
@login_required
def dashboard_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        fitness_level = user_profile.fitness_level
        fitness_level_display = user_profile.get_fitness_level_display()
    except UserProfile.DoesNotExist:
        fitness_level = None
        fitness_level_display = 'تعیین نشده'

    return render(request, 'fitness_app/dashboard.html', {
        'fitness_level': fitness_level,
        'fitness_level_display': fitness_level_display,
    })


# صفحات تمرین
@login_required
def beginner_training(request):
    return render(request, 'fitness_app/training_beginner.html')

@login_required
def intermediate_training(request):
    return render(request, 'fitness_app/training_intermediate.html')

@login_required
def advanced_training(request):
    return render(request, 'fitness_app/training_advanced.html')


# صفحات تغذیه
@login_required
def beginner_nutrition(request):
    return render(request, 'fitness_app/nutrition_beginner.html')

@login_required
def intermediate_nutrition(request):
    return render(request, 'fitness_app/nutrition_intermediate.html')

@login_required
def advanced_nutrition(request):
    return render(request, 'fitness_app/nutrition_advanced.html')


# مسیر داینامیک تمرین با level
@login_required
def workout_view(request, level):
    templates = {
        'beginner': 'fitness_app/training_beginner.html',
        'intermediate': 'fitness_app/training_intermediate.html',
        'advanced': 'fitness_app/training_advanced.html',
    }
    template = templates.get(level)
    if template:
        return render(request, template)
    else:
        raise Http404("سطح تمرین نامعتبر است.")


# مسیر داینامیک تغذیه با level
@login_required
def nutrition_view(request, level):
    templates = {
        'beginner': 'fitness_app/nutrition_beginner.html',
        'intermediate': 'fitness_app/nutrition_intermediate.html',
        'advanced': 'fitness_app/nutrition_advanced.html',
    }
    template = templates.get(level)
    if template:
        return render(request, template)
    else:
        raise Http404("سطح تغذیه نامعتبر است.")


# فرم تماس با ما
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'fitness_app/contact.html', {'form': form})
