from django.test import TestCase, Client
from .models import User
from .forms import UserRegisterForm

class UserModelTests(TestCase):
    def setUp(self):
        self.test_user_info = {
            'username':'test_user',
            'email':'test_email@stein.com',
            'password':'124qew34q',
        }

    def test_unique_username_required(self):
        '''Tests that multiple users can't be created with the same username'''     
        try:
            not_unique_username1 = User.objects.create_user(
                'not_unique_username', self.test_user_info['password'])
            not_unique_username2 = User.objects.create_user(
                'not_unique_username', self.test_user_info['password'])
        except:
            duplicate_username_created = False
        else:
            duplicate_username_created = True
        self.assertFalse(duplicate_username_created)

    def test_unique_slug_required(self):
        '''Tests that multiple users can't be created with the same slug'''       
        test_slug_1 = User.objects.create_user(
            'test_username_1', self.test_user_info['password'], slug='test_duplicate_slug'
        )
        test_slug_2 = User.objects.create_user(
            'test_username_2', self.test_user_info['password'], slug='test_duplicate_slug'
        )
        self.assertNotEqual(test_slug_1.slug, test_slug_2.slug)

    def test_user_object_create(self):
        '''Tests if an object can be created with the User model'''
        try:
            self.test_user = User.objects.create_user(
                self.test_user_info['username'], self.test_user_info['password'])
        except Exception as e:
            print(f'Object could not be created with the User model. ERROR: {e}')
        self.assertIsNotNone(self.test_user)


class ProfileFormsTests(TestCase):
    def test_UserRegisterForm(self):
        '''Tests that the UserRegisterForm takes valid data.'''
        data = {
            'username':'test_user',
            'password1':'124qew34q',
            'password2':'124qew34q',
            'email':'test_email@stein.com',
            'slug':'test_user',
        }
        try:
            form = UserRegisterForm(data)
        except Exception as e:
            print(f'Couldn\'t create form. ERROR: {e}')
        self.assertTrue(form.is_valid())


class ProfileViewsTests(TestCase):
    def setUp(self):
        self.test_user_info = {
            'username':'test_user',
            'email':'test_email@stein.com',
            'password':'124qew34q',
            'slug':'test_user',
        }
        self.test_user = User.objects.create_user(
            self.test_user_info['username'],
            self.test_user_info['email'],
            self.test_user_info['password'],
            slug=self.test_user_info['slug'],
        )
        self.client = Client()

    def test_signup_get(self):
        '''Test if the user register page loads properly'''
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_UserCreateView_post(self):
        '''Tests that the UserCreateView creates a new user.'''
        user_registration_info = {
            'username': self.test_user_info['username'],
            'email': self.test_user_info['email'],
            'password1': self.test_user_info['password'],
            'password2': self.test_user_info['password'],
            }
        self.client.post('/signup/', user_registration_info, follow=True)
        created_user = User.objects.get(username=user_registration_info['username'])
        self.assertIsNotNone(created_user)

    def test_login_get(self):
        '''Test if the user login page loads properly'''
        response = self.client.get('/profile/login/')
        self.assertEqual(response.status_code, 200)

    def test_UserLoginView_valid_post(self):
        '''Tests that the login view allows users to log in with valid credentials.'''
        user_credentials = {'username': self.test_user_info['username'], 'password': self.test_user_info['password']}
        response = self.client.post('/profile/login/', user_credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_UserLoginView_invalid_post(self):
        '''Tests that the login view does not allow user to log in with invalid credentials.'''
        user_credentials = {'username': self.test_user_info['username'], 'password': '12gt45k9'}
        response = self.client.post('/profile/login/', user_credentials, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_UserDetailView_get(self):
        '''Test if the profile detail view page loads properly'''
        response = self.client.get('/profile/test_user/')
        self.assertEqual(response.status_code, 200)

    def test_profile_update_get(self):
        '''Test if the profile update page loads properly'''
        response = self.client.get('/profile/test_user/update/')
        self.assertEqual(response.status_code, 200)

    def test_UserUpdateView(self):
        '''Test that UserUpdateView changes the user object with valid POST data'''
        user_update_info = {
            'username':'test_user',
            'email':'new_test_email@stein.com',
        }
        self.client.post(f'/profile/{self.test_user.slug}/update/', user_update_info, follow=True)
        self.test_user.refresh_from_db()
        self.assertEqual(self.test_user.email, user_update_info['email'])

    def test_logout_get(self):
        '''Test if the user logout gives proper response code'''
        response = self.client.get('/profile/logout/')
        self.assertEqual(response.status_code, 302) #302 for a redirect

    def test_logout_redirect_get(self):
        '''Test if the user logout url redirects to the correct url'''
        response = self.client.get('/profile/logout/')
        self.assertEqual(response.url, '/profile/login/')

    def test_UserLogoutView_post(self):
        '''Test if the logout view logs the user out.'''
        user_credentials = {'username': self.test_user_info['username'], 'password': self.test_user_info['password']}
        self.client.post('/profile/login/', user_credentials, follow=True)
        response = self.client.post('/profile/logout/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
