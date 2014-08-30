from django.db import models
from precisely import settings

import datetime

def pdf_file_name(instance, filename):
    x = '_'.join([filename.replace(" ", "_").replace("/", "_")])
    return '/'.join(['SignPDF', instance.receiver_email.replace(" ", "_").replace("@", "_"), x])

class Document(models.Model):
    is_signed = models.BooleanField(default=False)
    date_modified = models.DateTimeField(null=True, blank=True, default=datetime.datetime.today(), auto_now=True, auto_now_add=True)
    receiver = models.CharField(max_length=128, blank=False, null=False)
    receiver_email = models.CharField(max_length=128, blank=False, null=False)    
    pdf = models.FileField(max_length=512, upload_to=pdf_file_name, null=True, blank=True)
    signature_request_id = models.CharField(max_length=128, blank=True, null=True)

    def get_file_url(self):
        if settings.LOCALHOST:
            return 'https://drive.google.com/file/d/0B0LIuW1RdH4XYl9vVHNJZ0JqMGc/edit?usp=sharing'
        return ''.join([settings.DEPLOYED_ADDRESS, self.pdf.url])
