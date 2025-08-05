from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, ContactMessage

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    fitness_level = forms.ChoiceField(choices=UserProfile.LEVEL_CHOICES, label="سطح تمرینی")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # رمز عبور را هش می‌کند
        if commit:
            user.save()
            # ساخت پروفایل کاربری همراه با انتخاب سطح تمرینی
            UserProfile.objects.create(user=user, fitness_level=self.cleaned_data['fitness_level'])
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'message': 'پیام',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
