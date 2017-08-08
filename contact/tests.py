from django.test import TestCase
from .views import contact
from django.core.urlresolvers import resolve

 
class ContactTest(TestCase):
    def test_contact_resolves(self):
        contact_page = resolve('/contact/')
        self.assertEqual(contact_page.func, contact)


    def test_contact_status_code_is_ok(self):
        contact_page = self.client.get('/contact/')
        self.assertEqual(contact_page.status_code, 200)



