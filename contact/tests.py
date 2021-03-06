from django.test import TestCase
from django.conf import settings
from .forms import ContactForm

class ContactFormTests(TestCase):
    def test_contact_form_invalid_email(self):
        '''Test to make sure the form won't accept invalid email'''
        form = ContactForm(data={'from_name': 'testname',
                                    'from_email': 'testthisform&&gmail.com',
                                    'subject': 'test subject',
                                    'contact_message': 'random words for testing',
                                    })
        self.assertEqual(
            form.errors["from_email"], ["Enter a valid email address."]
        )
        
class ContactViewTests(TestCase):
    def test_contact_form_get(self):
        '''Test if the form page loads properly with GET request'''
        response = self.client.get('/contact/')
        self.assertEqual(
            response.status_code, 200
        )

    # This test does not work due to recaptcha
    # def test_contact_form_post_success(self):
    #     '''Test if the form will can take valid information'''
    #     data = {'from_name': 'testname',
    #                 'from_email': 'testthisform@gmail.com',
    #                 'subject': 'test subject',
    #                 'contact_message': 'random words for testing',
    #                 }
    #     form = ContactForm(data)
    #     self.assertEqual(form.is_valid(), True)
