from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from faker import Faker


class TestContact(TestCase):

    def test_contact_is_valid(self):
        data = {
            'email': 'darahcook@sanchez-brown.biz',
            'subject': 'subject',
            'text': 'text',
        }
        response = self.client.post(reverse('contact'), data)
        assert response.status_code in [301, 302]
        # self.assertEqual(response.status_code==302)

        data['email'] = 'WRONG'
        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 200


class TestStudents(TestCase):
    fake = Faker()
    # fixtures = ['db.json']

    def setUp(self) -> None:
        print('Setup')

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'db.json', verbosity=0)
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def _gen_data(self):
        return {
            'subject': self.fake.word(),
            'text': self.fake.text(),
        }

    def test_contact_form(self):
        from students.models import Student
        data = {
            'email': self.fake.email(),
            **self._gen_data(),
        }
        # data.update(self._gen_data())
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 302

    def test_contact_form_wrong_email(self):
        data = {
            'email': 'wrong_email',
            **self._gen_data(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200

    def test_contact_form_empty_subject(self):
        data = {
            'email': self.fake.email(),
            'subject': '',
            'text': self.fake.text(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200
