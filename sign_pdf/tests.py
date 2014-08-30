import datetime
from django.test import TestCase, Client
from sign_pdf.models import *
from sign_pdf.views import *
from django.test.client import RequestFactory
import requests

class PDFTest(TestCase):

    def setUp(self):
        doc = Document()
        doc.receiver_email = 'a@b.com'
        doc.receiver = 'john'
        doc.signature_request_id = 'test'
        doc.save()
    
    def tearDown(self):
        Document.objects.all().delete()

    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_update_file(self):
        c = Client()
        doc = Document.objects.get(signature_request_id='test')
        self.assertEqual(doc.is_signed, False)
        response = c.get('/signed/?event=signature_request_signed&signature_id=test')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200)
        self.assertEqual(doc.is_signed, True)
