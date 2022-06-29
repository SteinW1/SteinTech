from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, FormView
from .models import User
from .forms import LoginForm

def UserLogoutView(request):
    context={}
    logout(request)
    return redirect('user-login')

class UserLoginView(FormView):
    model = User
    form_class = LoginForm
    success_url = '/'
    success_url = '/'
    template_name = 'users/user_login.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, user)
        return super().form_valid(form)

class UserDetailView(DetailView):
    model = User
    print(User.username)
    slug_field = User.username
    context_object_name = "user"
    template_name = 'users/user_detail.html'
