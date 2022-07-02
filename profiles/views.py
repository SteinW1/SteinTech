from django.shortcuts import redirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView, UpdateView, FormView
from .forms import UserRegisterForm
from .models import User

def UserLogoutView(request):
    logout(request)
    return redirect('profile-login')

class UserLoginView(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'profiles/user_login.html'
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'You\'re now logged in.')
            return super().form_valid(form)
        else:
            messages.error(self.request, f'Failed to log in.')
            return redirect('user-login')

class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = 'profiles/user_detail.html'

class UserCreateView(FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'profiles/user_register.html'
    success_url = '/profile/login/'

    def form_valid(self, form):
        form.cleaned_data['user'] = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            slug=slugify(form.cleaned_data['username']),
            )
        messages.success(self.request, f'New profile created. You may now log in.')
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    fields = [
        'username',
        'email',
    ]
    template_name_suffix = '_update_form'
