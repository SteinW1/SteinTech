from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic import FormView
from .forms import ContactForm
from requests import post as send_post_request 

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/contact/' 

    def get_context_data(self, **kwargs):
        return super().get_context_data(recaptcha_site_key = settings.RECAPTCHA_SITE_KEY, **kwargs)

    def form_valid(self, form):
        if validateRecaptcha(self.request):                              
            try:
                send_mail(
                    form.cleaned_data['subject'],
                    form.cleaned_data['message'],
                    form.cleaned_data['from_email'],
                    ['admin@williamstein.com'],
                    )
            except BadHeaderError:
                messages.error(self.request, f'Invalid header found.')
            messages.success(self.request, f'Thank you, your message has been sent!')
        else:
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
        return super().form_valid(form)

def validateRecaptcha(request) -> bool:
    '''Function for validating a POST request with google's reCAPTCHA.'''    
    data = {'secret': settings.RECAPTCHA_SECRET_KEY, 'response': request.POST.get('g-recaptcha-response')}
    reCAPTCHA_result = send_post_request('https://www.google.com/recaptcha/api/siteverify', data=data).json()
    return reCAPTCHA_result['success']
