from django.shortcuts import redirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, UpdateView, FormView
from .forms import LoginForm, UserRegisterForm
from .models import User

def UserLogoutView(request):
    logout(request)
    return redirect('user-login')

class UserLoginView(FormView):
    model = User
    form_class = LoginForm
    success_url = '/'
    template_name = 'profiles/user_login.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user and user.is_authenticated:
            login(self.request, user)
            messages.success(self.request, f'You\'re now logged in.')
        else:
            messages.error(self.request, f'Failed to log in.')
            return redirect('user-login')
        return super().form_valid(form)

class UserDetailView(DetailView):
    model = User
    print(User.username)
    slug_field = User.username
    context_object_name = "user"
    template_name = 'profiles/user_detail.html'

class UserCreateView(FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'profiles/user_register.html'
    success_url = '/welcome/'

    def form_valid(self, form):
        slug = slugify(form.cleaned_data['username'])
        if form.cleaned_data['password1'] == form.cleaned_data['password2']:
            form.cleaned_data['user'] = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1'],
                slug=slug,
                )
        messages.success(self.request, f'New profile created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, f'Profile could not be created.')
        response = super().form_invalid(form)
        return response